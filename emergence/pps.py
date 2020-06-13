import numpy as np
import matplotlib.pyplot as plt
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage
import sys

class PPS(object):
    ''' Primordial Particle Systems
    '''
    def __init__(self, size=200, density=0.1, alpha=180, beta=17, v=0.3, r=7.6):
        self.alpha = alpha
        self.beta = beta
        self.v = v
        self.r = r
        self.size = size
        number = int(size**2*density)
        self.pos = np.random.uniform(0,size,(number,2))
        self.phi = 180*np.random.randn(number)
        self.N = np.zeros((number))
        self.D = np.zeros((number))
        self.fig, self.ax = plt.subplots()
        self.fig.patch.set_facecolor('black')
        self.fig.set_size_inches(10.5, 10.5, forward=True)
        
    def __len__(self):
        return self.pos.shape[0]
    
    def angle2vec(self, angle):
        return np.array([np.cos(angle/360*2*np.pi), np.sin(angle/360*2*np.pi)])
    
    def update(self):
        for i in range(len(self)):
            distance = np.linalg.norm(self.pos - self.pos[i], axis=1)
            self.D[i] = np.sum(distance < 1.3)
            particles = self.pos[np.logical_and(0 < distance, distance < self.r)]  
            angle = np.sign(np.cross(self.angle2vec(self.phi[i]), particles-self.pos[i]))
            L = np.sum(angle > 0)
            R = np.sum(angle < 0)
            self.N[i] = L + R
            self.phi[i] += self.alpha + self.beta * self.N[i] * np.sign(R-L)
            self.pos[i] += self.angle2vec(self.phi[i]) * self.v

    def visualize(self, t):
        if t % 1 == 0:
            self.ax.clear()
            plt.title('PPS Model')
            pos = self.pos[self.N < 17]
            plt.scatter(pos[:,0], pos[:,1], c="green", s=5)
            pos = self.pos[np.all([17 < self.N, self.N <= 35], axis=0)]
            plt.scatter(pos[:,0], pos[:,1], c="blue", s=5)
            pos = self.pos[35 < self.N]
            plt.scatter(pos[:,0], pos[:,1], c="yellow", s=5)
            pos = self.pos[10 < self.D]
            plt.scatter(pos[:,0], pos[:,1], c="magenta", s=5)
            
            plt.axis('off')
            plt.draw()
            plt.xlim(10,self.size-10)
            plt.ylim(10,self.size-10)
            self.fig.canvas.mpl_connect('close_event', self.handle_close)
            plt.pause(.001)

    def animation(self, t):
        self.update()
        self.ax.clear()
        pos = self.pos[self.N < 17]
        plt.scatter(pos[:,0], pos[:,1], c="green", s=5)
        pos = self.pos[np.all([17 < self.N, self.N <= 35], axis=0)]
        plt.scatter(pos[:,0], pos[:,1], c="blue", s=5)
        pos = self.pos[35 < self.N]
        plt.scatter(pos[:,0], pos[:,1], c="yellow", s=5)
        pos = self.pos[10 < self.D]
        plt.scatter(pos[:,0], pos[:,1], c="magenta", s=5)
        plt.axis('off')
        plt.xlim(10,self.size-10)
        plt.ylim(10,self.size-10)
        return mplfig_to_npimage(self.fig)

    def handle_close(self, evt):
        sys.exit()

if __name__ == '__main__':
    model = PPS()
    # for i in range(10000):
    #     model.visualize(i)
    #     model.update()

    animation = VideoClip(model.animation, duration=150)
    animation.write_videofile('pps.mp4', fps=20)