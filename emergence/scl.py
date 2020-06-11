# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import sys

HOLE = 0
CATALYST = 1
SUBSTRATE = 2
LINK = 3
BOND_LINK = 4 # 4 or 5

SPACE_SIZE = 64
# 初期化設定に関するパラメタ
INITIAL_SUBSTRATE_DENSITY = 0.8
INITIAL_CATALYST_POSITIONS = [8,8]

MOBILITY_FACTOR = {
    HOLE:           0.1,
    SUBSTRATE:      0.1,
    CATALYST:       0.0001,
    LINK:           0.05,
    BOND_LINK:      0.05,}
PRODUCTION_PROBABILITY             = 0.95
DISINTEGRATION_PROBABILITY         = 0.0005
BONDING_CHAIN_INITIATE_PROBABILITY = 0.1
BONDING_CHAIN_EXTEND_PROBABILITY   = 0.6
BONDING_CHAIN_SPLICE_PROBABILITY   = 0.9
BOND_DECAY_PROBABILITY             = 0.0005
ABSORPTION_PROBABILITY             = 0.5
EMISSION_PROBABILITY               = 0.5

def get_neumann_neighborhood(x, y, space_size):
    n = [((x+0.5)%space_size, y), ((x-0.5)%space_size, y), (x, (y+0.5)%space_size), (x, (y-0.5)%space_size)]
    return n

def get_moore_neighborhood(x, y, space_size):
    n = [((x-1)%space_size, (y-1)%space_size), (x, (y-1)%space_size), ((x+1)%space_size, (y-1)%space_size), \
         ((x-1)%space_size,  y              ),                        ((x+1)%space_size,  y              ), \
         ((x-1)%space_size, (y+1)%space_size), (x, (y+1)%space_size), ((x+1)%space_size, (y+1)%space_size)]
    return n

def neumann_neighborhood(particles, x, y):
    """
    """
    neighborhood = [((x+1)%particles.shape[0], y), ((x-1)%particles.shape[0], y), (x, (y+1)%particles.shape[0]), (x, (y-1)%particles.shape[0])]
    mask = np.array([particles[i[0], i[1]] for i in neighborhood]) <= LINK
    result = np.array(neighborhood)[mask]
    if len(result) < 1:
        return None
    return result[np.random.choice(len(result), 1, replace=False)][0]

def moore_neighborhood_subs(particles, x, y):
    """
    get random two SUBSTRATEs in moore neighborhood
    """
    neighborhood = get_moore_neighborhood(x, y, particles.shape[0])
    mask = np.array([particles[i[0], i[1]] for i in neighborhood]) == SUBSTRATE
    result = np.array(neighborhood)[mask]
    if len(result) < 2:
        return None, None
    return result[np.random.choice(len(result), 2, replace=False)]

def moore_neighborhood_link(particles, x, y):
    """
    get random LINK in moore neighborhood
    """
    neighborhood = get_moore_neighborhood(x, y, particles.shape[0])
    mask1 = np.array([particles[i[0], i[1]] for i in neighborhood]) == LINK
    mask2 = np.array([particles[i[0], i[1]] for i in neighborhood]) == BOND_LINK
    if np.sum(mask2) > 0 and np.random.rand() < 0.8:
        result = np.array(neighborhood)[mask2]
    else:
        result = np.array(neighborhood)[np.logical_or(mask1, mask2)]
    if len(result) < 1:
        return None
    return result[np.random.choice(len(result), 1, replace=False)][0]

def moore_neighborhood_hole(particles, x, y):
    """
    get random HOLE in moore neighborhood
    """
    neighborhood = get_moore_neighborhood(x, y, particles.shape[0])
    mask = np.array([particles[i[0], i[1]] for i in neighborhood]) == HOLE
    result = np.array(neighborhood)[mask]
    if len(result) < 1:
        return None
    return result[np.random.choice(len(result), 1, replace=False)][0]

def is_in_moor_neighborhood(particles, x, y, type):
    neighborhood = get_moore_neighborhood(x, y, particles.shape[0])
    mask = np.array([particles[i[0], i[1]] for i in neighborhood]) == type
    return np.any(mask)

def composition(particles, probability):
    """
    2S + C -> L + C
    """
    idx = np.where(particles == CATALYST)
    for i, j in zip(*idx):
        n1, n2 = moore_neighborhood_subs(particles, i, j)
        if n1 is None or n2 is None:
            continue
        if np.random.rand() < probability:
            particles[n1[0], n1[1]] = HOLE
            particles[n2[0], n2[1]] = LINK

def bonding(particles, bonds, init_prob, splice_prob, ext_prob):
    """
    L + L -> BL (bond)
    """
    idx = np.where(np.logical_or(particles == LINK, particles == BOND_LINK))
    for i, j in zip(*idx):
        n = moore_neighborhood_link(particles, i, j)
        if n is None:
            continue
        # can't bond if there is neighboring CATALYST
        if is_in_moor_neighborhood(particles, i, j, CATALYST) or is_in_moor_neighborhood(particles, n[0], n[1], CATALYST):
            continue
        # # can't bond if neighboring LINK has more than two connections
        if particles[n[0], n[1]] < BOND_LINK and is_in_moor_neighborhood(particles, n[0], n[1], BOND_LINK+1):
            continue
        if particles[n[0], n[1]] == BOND_LINK + 1:
            continue
        # don't allow crossing
        if hash(f"{[(i+n[0])/2, (j+n[1])/2]}") in bonds:
            continue
        # make sure the bonding angle is no less than 90 degrees
        flag = False
        for l in get_neumann_neighborhood((i+n[0])/2, (j+n[1])/2, particles.shape[0]):
            if hash(f"{[l[0], l[1]]}") in bonds:
                flag = True
        if flag:
            continue
        if particles[i,j] == LINK and particles[n[0], n[1]] == LINK:
            probability = init_prob
        elif particles[i,j] == BOND_LINK and particles[n[0], n[1]] == BOND_LINK:
            probability = splice_prob
        else:
            probability = ext_prob
        if np.random.rand() < probability:
            particles[i, j] += 1
            particles[n[0], n[1]] += 1
            bonds.update({hash(f"{[(i+n[0])/2, (j+n[1])/2]}"): [[i, n[0]],[j, n[1]]]})
        
def disintegration(particles, probability):
    """
    L -> 2S
    """
    idx = np.where(particles == LINK)
    for i, j in zip(*idx):
        n = moore_neighborhood_hole(particles, i, j)
        if n is None:
            continue
        if np.random.rand() < probability:
            particles[i, j] = SUBSTRATE
            particles[n[0], n[1]] = SUBSTRATE

def bond_decay(particles, bonds, probability):
    """
    BL -> L + L
    """
    idx = np.where(particles >= BOND_LINK)
    for i, j in zip(*idx):
        if particles[i, j] < BOND_LINK:
            continue
        if np.random.rand() < probability:
            neighborhood = get_moore_neighborhood(i, j, particles.shape[0])
            for n in neighborhood:
                if hash(f"{[(i+n[0])/2, (j+n[1])/2]}") in bonds:
                    particles[i, j] -= 1
                    particles[n[0], n[1]] -= 1
                    if particles[i, j] < 2: particles[i,j] = 2
                    if particles[n[0], n[1]] < 2: particles[n[0],n[1]] = 2
                    bonds.pop(hash(f"{[(i+n[0])/2, (j+n[1])/2]}"))
                    break

def move(particles, bonds):
    idx = np.where(particles <= LINK)
    moved = np.zeros_like(particles)
    for i, j in zip(*idx):
        if moved[i,j] == 1:
            continue
        n = neumann_neighborhood(particles, i, j)
        if n is None:
            continue
        if particles[n[0], n[1]] > LINK:
            continue

        if np.random.rand() < np.sqrt(MOBILITY_FACTOR[particles[i,j]]*MOBILITY_FACTOR[particles[n[0], n[1]]]):
            particles[i,j], particles[n[0], n[1]] = particles[n[0], n[1]], particles[i,j]
        moved[i,j] = 1
        moved[n[0],n[1]] = 1

class SCL(object):
    def __init__(self, space_size, num_catalyst=3):
        x = np.linspace(0, space_size-1, space_size)
        y = np.linspace(0, space_size-1, space_size)
        self.xx, self.yy = np.meshgrid(x, y)
        self.bonds = {}
        self.particles = np.zeros((space_size, space_size))
        self.particles = np.zeros((space_size,space_size))
        self.particles[np.random.rand(space_size,space_size) < INITIAL_SUBSTRATE_DENSITY] = SUBSTRATE
        for i in range(num_catalyst):
            self.particles[np.random.randint(4,space_size-4),np.random.randint(4,space_size-4)] = CATALYST

        self.fig, self.ax = plt.subplots()

    def update(self):
        # move particles
        move(self.particles, self.bonds)
        # reactions
        composition(self.particles, PRODUCTION_PROBABILITY)
        disintegration(self.particles, DISINTEGRATION_PROBABILITY)
        bonding(self.particles, self.bonds, BONDING_CHAIN_INITIATE_PROBABILITY, BONDING_CHAIN_SPLICE_PROBABILITY, BONDING_CHAIN_EXTEND_PROBABILITY)
        bond_decay(self.particles, self.bonds, BOND_DECAY_PROBABILITY)

    def visualize(self, t):
        if t % 10 == 0:
            self.ax.clear()
            plt.title('SCL Model')
            mask = self.particles == SUBSTRATE
            plt.scatter(self.xx[mask],self.yy[mask],c="lightgreen",s=10)
            mask = self.particles == CATALYST
            plt.scatter(self.xx[mask],self.yy[mask],c="red",s=40)
            mask = self.particles == LINK
            plt.scatter(self.xx[mask],self.yy[mask], facecolors="none", edgecolors="blue", s=30, marker="s")
            for link in self.bonds.values():
                plt.plot(link[1], link[0], color="blue")
            mask = self.particles == BOND_LINK
            plt.scatter(self.xx[mask],self.yy[mask], facecolors="white", edgecolors="blue", s=30, marker="s")
            mask = self.particles == BOND_LINK + 1
            plt.scatter(self.xx[mask],self.yy[mask], facecolors="white", edgecolors="red", s=30, marker="s")
            mask = self.particles > BOND_LINK + 1
            plt.scatter(self.xx[mask],self.yy[mask], facecolors="white", edgecolors="black", s=30, marker="s")
            
            plt.axis('off')
            plt.draw()
            self.fig.canvas.mpl_connect('close_event', self.handle_close)
            plt.pause(.001)

    def handle_close(self, evt):
        sys.exit()

if __name__ == '__main__':
    model = SCL(32)
    for i in range(100000):
        model.update()
        model.visualize(i)
    raise