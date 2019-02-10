## Overview

In 1952, [Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing) published a paper, "[The Chemical Basis of Morphogenesis](http://www.dna.caltech.edu/courses/cs191/paperscs191/turing.pdf)," which mathematically demonstrated the main phenomena of morphogenesis. In the paper he introduced a concept of morphogens, which is a system of chemical substances reacting together and diffusing through a tissue, and demonstrated the main phenomena of morphogenesis with series of equations that morphogens obay for its interaction. Due to an instability of the homogeneous equilibrium, a reaction-diffusion system can produce a pattern or structure. This section will get into the emergent phenomenon in patterns.

## Gray Scott Model of Reaction Diffusion

Gray Scott model describes the variation of u and v, which represent the concentration of chemical U and V respectively. U and V react according the following equation:

<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?U&plus;2V\rightarrow&space;3V" title="U+2V\rightarrow 3V" />
</p>
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?V\rightarrow&space;P" title="V\rightarrow P" />
</p>
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;u}{\partial&space;t}&space;=&space;D_u\triangledown^2u&space;-&space;uv^2&space;&plus;&space;F(1-u)" title="\frac{\partial u}{\partial t} = D_u\triangledown^2 - uv^2 + F(1-u)" />
</p>
<p align="center">
  <img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;v}{\partial&space;t}&space;=&space;D_v\triangledown^2v&space;+&space;uv^2&space;-&space;(F&plus;k)v" title="\frac{\partial v}{\partial t} = D_v\triangledown^2v - uv^2 - (F+k)v" />
</p>

This model can be seen as a simulation of the behavior of diffusive living things reproducing under conditions of limited food. Different patterns emerge for slight changes in feeding and death rates.

[source](/patterns/gray_scott.py)

### self-replicating spots (f=0.022, k=0.05)
This pattern can be seen in Hawaiian Whitespotted Toby.
<p align="center">
  <img src="https://mauioceancenter.com/wp-content/uploads/2017/09/White-Spotted-Toby-web-1-768x512.jpg" height="200"/>
  <img src="https://github.com/Kashu7100/Recreation-of-Nature/blob/master/assets/self_replacing_spots.png" height="200"/>
</p>

### stable spots (f=0.035, k=0.065)
This pattern can be seen in Puffer Fish.
<p align="center">
  <img src="https://foodsafetynewsfullservice.marlersites.com/files/2014/01/puffer-fish-406-2.jpg" height="200"/>
  <img src="https://github.com/Kashu7100/Recreation-of-Nature/blob/master/assets/stable_spots.png" width="200"/>
</p>

### unstable spots (f=0.012, k=0.05)
This pattern can be seen in Spotted Eagle Ray.
<p align="center">
  <img src="http://www.animalspot.net/wp-content/uploads/2012/01/Spotted-eagle-ray-Photos.jpg" height="200"/>
  <img src="https://github.com/Kashu7100/Recreation-of-Nature/blob/master/assets/unstable_spots.png" width="200"/>
</p>

### Labyrinthine pattern (f=0.04, k=0.06)
This pattern can be seen in Brain Coral.
<p align="center">
  <img src="https://oceana.org/sites/default/files/styles/lightbox/public/shutterstock_260309279.jpg" height="200"/>
  <img src="https://github.com/Kashu7100/Recreation-of-Nature/blob/master/assets/labyrinthine_pattern.png" width="200"/>
</p>

### Worm-like pattern (f=0.042, k=0.064)
This pattern can be seen in Burrfish.
<p align="center">
  <img src="https://scaquarium.org/wp-content/uploads/2015/11/sc-aquarium-burrfish-animal-spec-sheet.jpg" height="200"/>
  <img src="https://github.com/Kashu7100/Recreation-of-Nature/blob/master/assets/worm_like_pattern.png" width="200"/>
</p>
