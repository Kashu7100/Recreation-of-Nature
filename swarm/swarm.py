import numpy as np
import vispy
import random
from vispy import app
from vispy.scene import SceneCanvas
from vispy.scene import visuals
from vispy.gloo.util import _screenshot

class Agents(object):
    ''' Agents class\n
    Representation of a group of agent with same parameters.
    Args:
        number (int): number of agents in this group
        dim (int): dimention of the space; chose 2 or 3
        cohesion_force (double): determines the tendency of an agent to move towards the center of the group
        separation_force (double): determines the tendency of an agent to move away from other agents in the group
        alignment_force (double): determines the tendency of an agent to face the same direction as the sorrounding agents
        attack_force (double): determines the tendency of an agent to attack other agents (prey) in different groups
        escape_force (double): determines the tendency of an agent to escape from ohter agents (predator) in different groups
        cohesion_dist (double): determines the range of an agent to move towards the center of the group
        separation_dist (double): determines the range of an agent to move away from other agents in the group
        alignment_dist (double): determines the range of an agent to face the same direction as the sorrounding agents
        attack_dist (double): determines the range of an agent to attack other agents (prey) in different groups
        escape_dist (double): determines the range of an agent to escape from ohter agents (predator) in different groups
        cohesion_angle (double): determines the effenctive angle of an agent to move towards the center of the group
        separation_angle (double): determines the effenctive angle of an agent to move away from other agents in the group
        alignment_angle (double): determines the effenctive angle of an agent to face the same direction as the sorrounding agents
        max_speed (double): defines maximum speed of the agents
        min_speed (double): defines minimum speed of the agents
        boundary_force (double): affects an agent get out of the boundary
        boundary (double): defines the boundary of free space
    '''
    def __init__(self, number, dim=3, cohesion_force=0.01, separation_force=0.4, alignment_force=0.001, attack_force=0.005, escape_force=0.0025,
                    cohesion_dist=0.5, separation_dist=0.05, alignment_dist=0.05, attack_dist=0.3, escape_dist=0.5,
                    cohesion_angle=np.pi/2, separation_angle=np.pi/2, alignment_angle=np.pi/3,
                    max_speed=0.03, min_speed=0.005, boundary_force=0.003, boundary=1):
        self.cohesion = [cohesion_force, cohesion_dist, cohesion_angle]
        self.separation = [separation_force, separation_dist, separation_angle] 
        self.alignment = [alignment_force, alignment_dist, alignment_angle]
        self.attack = [attack_force, attack_dist]
        self.escape = [escape_force, escape_dist]
        self.max_speed = max_speed
        self.min_speed = min_speed
        self.dim = dim
        self.pos = np.random.randn(number,dim)
        self.vel = np.random.randn(number,dim) * self.min_speed
        self.boundary_force = boundary_force
        self.boundary = boundary

    def __len__(self):
        return self.pos.shape[0]
    
    def update(self, predator=None, prey=None):
        for i in range(len(self)):
            distance = np.linalg.norm(self.pos - self.pos[i], axis=1)
            angle = np.arccos(np.dot(self.vel[i], (self.pos-self.pos[i]).T) / (np.linalg.norm(self.vel[i]) * np.linalg.norm((self.pos-self.pos[i]), axis=1)))
            cohesion_agents = self.pos[np.all([0 < distance, distance < self.cohesion[1], angle < self.cohesion[2]], axis=0)]
            separation_agents = self.pos[np.all([distance < self.separation[1], angle < self.separation[2]], axis=0)]
            alignment_agents = self.vel[np.all([0 < distance, distance < self.alignment[1], angle < self.alignment[2]], axis=0)]
            if len(cohesion_agents) > 0:
                self.vel[i] += self.cohesion[0] * (np.mean(cohesion_agents, axis=0) - self.pos[i])
            if len(separation_agents) > 0:
                self.vel[i] += self.separation[0] * np.sum(separation_agents - self.pos[i], axis=0)
            if len(alignment_agents) > 0:
                self.vel[i] += self.alignment[0] * (np.mean(alignment_agents, axis=0) - self.vel[i])
            if self.boundary_force > 0 and np.linalg.norm(self.pos[i]) > self.boundary:
                r = np.linalg.norm(self.pos[i])
                self.vel[i] -= self.boundary_force * self.pos[i] * (r - self.boundary) / r 
        if predator is not None:
            # escape from predator
            tmp_pos = self.pos
            tmp_vel = self.vel
            counter = 0
            for i in range(len(self)):
                targets = np.linalg.norm(predator.pos - self.pos[i], axis=1)
                if np.min(targets) > self.escape[1]:
                    continue
                elif np.min(targets) < 0.03 and np.all(np.random.rand(1) < 0.2):
                    tmp_pos = np.delete(tmp_pos, i - counter, 0)
                    tmp_vel = np.delete(tmp_vel, i - counter, 0)
                    counter += 1
                else:
                    tmp_vel[i - counter] += self.escape[0]*(self.pos[i] - predator.pos[np.argmin(targets)])/np.linalg.norm(self.pos[i] - predator.pos[np.argmin(targets)])**2
            self.pos = tmp_pos
            self.vel = tmp_vel
        if prey is not None:
            # eat prey
            for i in range(len(self)):
                targets = np.linalg.norm(prey.pos - self.pos[i], axis=1)
                if np.min(targets) > self.attack[1]:
                    continue
                else:
                    self.vel[i] += self.attack[0]*(prey.pos[np.argmin(targets)] - self.pos[i])/np.linalg.norm(prey.pos[np.argmin(targets)] - self.pos[i])**2
        for i in range(len(self)):
            v = np.linalg.norm(self.vel[i])
            if v < self.min_speed:
                self.vel[i] *= self.min_speed / v
            elif v > self.max_speed:
                self.vel[i] *= self.max_speed / v
        self.pos += self.vel
        result = np.repeat(self.pos, 2, axis=0)
        result[::2] -=  self.vel
        return result.reshape((-1, self.dim*2))

class Visualizer(object):
    '''Visualizer class\n
    Base class for the simulation of the swarm behavior.
    Args:
        width (int): defines the width of the window
        height (int): defines the height of the window
    '''
    def __init__(self, width=800, height=800):
        self.canvas = SceneCanvas(size=(width, height), position=(0,0), keys='interactive', title=self.__class__.__name__)
        self.view = self.canvas.central_widget.add_view()
        self.view.camera = 'turntable'
        self.axis = visuals.XYZAxis(parent=self.view.scene)
        self.canvas.show()

    def __bool__(self):
        return not self.canvas._closed

    def update(self):
        vispy.app.process_events()        
        self.canvas.update()

    def animation(self, t):
        self.update()
        return _screenshot((0,0,self.canvas.size[0],self.canvas.size[1]))[:,:,:3]
