import numpy as np
import matplotlib.pyplot as plt
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage

class GrayScott(object):
    def __init__(self, size=(256,256), Du=2e-5, Dv=1e-5, f=0.035, k=0.065):
        self.size = size
        self.Du = Du
        self.Dv = Dv
        self.f = f
        self.k = k
        self.u = np.ones(size) + np.random.rand(*size)/20
        self.v = np.zeros(size) + np.random.rand(*size)/20
        square = 20
        self.u[size[0]//2-square//2:size[0]//2+square//2,size[1]//2-square//2:size[1]//2+square//2] = 0.5
        self.v[size[0]//2-square//2:size[0]//2+square//2,size[1]//2-square//2:size[1]//2+square//2] = 0.25
        
        self.fig, self.ax = plt.subplots()

    def update(self):
        lu = np.zeros_like(self.u)
        lu[1:] += self.u[:-1]
        lu[:-1] += self.u[1:]
        lu[:,1:] += self.u[:,:-1]
        lu[:,:-1] += self.u[:,1:]
        lu -= 4*self.u
        lu /= 1e-4
        lv = np.zeros_like(self.v)
        lv[1:] += self.v[:-1]
        lv[:-1] += self.v[1:]
        lv[:,1:] += self.v[:,:-1]
        lv[:,:-1] += self.v[:,1:]
        lv -= 4*self.v
        lv /= 1e-4
        self.u += self.Du*lu - self.u*self.v**2 + self.f*(1-self.u)
        self.v += self.Dv*lv + self.u*self.v**2 - (self.f+self.k)*self.v

    def visualize(self, t):
        if t % 10 == 0:
            self.ax.clear()
            plt.title('Gray-Scott Model')
            self.ax.imshow(self.u, interpolation='nearest', cmap="nipy_spectral")
            plt.axis('off')
            plt.draw()
            plt.pause(.001)

    def animation(self, t):
        self.update()
        self.ax.clear()
        plt.title('Gray-Scott Model')
        self.ax.imshow(self.u, interpolation='nearest', cmap="nipy_spectral")
        plt.axis('off')
        return mplfig_to_npimage(self.fig)

if __name__ == '__main__':
    unstable_spots = GrayScott(f=0.012, k=0.05)
    for i in range(10000):
        unstable_spots.update()
        unstable_spots.visualize(i)
