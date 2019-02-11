import numpy as np
import matplotlib.pyplot as plt
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage

class GrayScott(object):
    def __init__(self, size=(256,256), Du=2e-5, Dv=1e-5, f=0.035, k=0.065, color='CMRmap'):
        self.size = size
        self.Du = Du
        self.Dv = Dv
        self.f = f
        self.k = k
        self.u = np.ones(size) + np.random.rand(*size)/20
        self.v = np.zeros(size) + np.random.rand(*size)/20
        self.color = color
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
            self.ax.imshow(self.u, interpolation='nearest', cmap=self.color)
            plt.axis('off')
            plt.draw()
            plt.pause(.001)

    def animation(self, t):
        self.update()
        self.ax.clear()
        plt.title('Gray-Scott Model')
        self.ax.imshow(self.u, interpolation='nearest', cmap=self.color)
        plt.axis('off')
        return mplfig_to_npimage(self.fig)
    
class FKmap(GrayScott):
    def __init__(self, size=(400,400), tile=10, Du=2e-5, Dv=1e-5, color='CMRmap'):
        super().__init__(size, Du, Dv, None, None, color)
        self.tile = tile
        self.f = np.zeros(size)
        self.k = np.zeros(size)
        self.init_f()
        self.init_k()
        
    def init_f(self):
        for n, i in enumerate(range(self.tile)):
            self.f[self.size[0]//self.tile*i:self.size[0]//self.tile*(i+1),:] = 0.004*n*10/self.tile
    
    def init_k(self):
        for n, i in enumerate(range(self.tile)):
            self.k[:,self.size[0]//self.tile*i:self.size[1]//self.tile*(i+1)] = 0.002*n*10/self.tile + 0.05

if __name__ == '__main__':
    unstable_spots = GrayScott(size=(400,400), f=0.012, k=0.05)
    for i in range(10000):
        unstable_spots.update()
        unstable_spots.visualize(i)
    
    # in order to save the animation, take out the comments below 
    #
    #animation = VideoClip(g.animation, duration=200)
    #animation.write_videofile('unstable_spots.mp4', fps=20)
