## Overview

In 1952, [Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing) published a paper, "[The Chemical Basis of Morphogenesis](http://www.dna.caltech.edu/courses/cs191/paperscs191/turing.pdf)," which mathematically demonstrated the main phenomena of morphogenesis. In the paper he introduced a concept of morphogens, which is a system of chemical substances reacting together and diffusing through a tissue, and demonstrated the morphogenesis phenomena with series of equations that morphogens obay for its interaction. Due to an instability of the homogeneous equilibrium, a reaction-diffusion system can produce a pattern or structure. This section will get into the emergent phenomenon in patterns.

## Gray Scott Model of Reaction Diffusion

Gray Scott model describes the variation of u and v, which represent the concentration of chemical U and V respectively. U and V react according the following equation:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=U %2B 2V \rightarrow 3V">
</p>
<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=V \rightarrow P">
</p>
<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\frac{\partial u}{\partial t} = D_u \triangledown^2u -uv^2 %2B F(1-u) ">
</p>
<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\frac{\partial v}{\partial t} = D_v \triangledown^2v %2B uv^2 -(F %2B k)v ">
</p>

This model can be seen as a simulation of the behavior of diffusive living things reproducing under conditions of limited food. Different patterns emerge for slight changes in feeding and death rates.

[[source code]](/patterns/gray_scott.py)

### self-replicating spots (f=0.022, k=0.05)
This pattern can be seen in Hawaiian Whitespotted Toby.
<p align="center">
  <img src="https://mauioceancenter.com/wp-content/uploads/2017/09/White-Spotted-Toby-web-1-768x512.jpg" height="200"/>
  <img src="/assets/self_replacing_spots.png" height="200"/>
  <br>
  <b> Figure 1: Hawaiian Whitespotted Toby</b> (retrieved from <a href="https://mauioceancenter.com">MAUI OCEAN CENTER</a>)
</p>

### stable spots (f=0.035, k=0.065)
This pattern can be seen in Puffer Fish.
<p align="center">
  <img src="https://foodsafetynewsfullservice.marlersites.com/files/2014/01/puffer-fish-406-2.jpg" height="200"/>
  <img src="/assets/stable_spots.png" width="200"/>
  <br>
  <b> Figure 2: Puffer Fish</b> (retrieved from <a href="https://foodsafetynewsfullservice.marlersites.com">FSN</a>)
</p>

### unstable spots (f=0.012, k=0.05)
This pattern can be seen in Spotted Eagle Ray.
<p align="center">
  <img src="http://www.animalspot.net/wp-content/uploads/2012/01/Spotted-eagle-ray-Photos.jpg" height="200"/>
  <img src="/assets/unstable_spots.png" width="200"/>
  <br>
  <b> Figure 3: Spotted Eagle Ray</b> (retrieved from <a href="http://www.animalspot.net">Animal Spot</a>)
</p>

### Labyrinthine pattern (f=0.04, k=0.06)
This pattern can be seen in Brain Coral.
<p align="center">
  <img src="https://oceana.org/sites/default/files/styles/lightbox/public/shutterstock_260309279.jpg" height="200"/>
  <img src="/assets/labyrinthine_pattern.png" width="200"/>
  <br>
  <b> Figure 4: Brain Coral</b> (retrieved from <a href="https://oceana.org">OCEANA</a>)
</p>

### Worm-like pattern (f=0.042, k=0.064)
This pattern can be seen in Burrfish.
<p align="center">
  <img src="https://scaquarium.org/wp-content/uploads/2015/11/sc-aquarium-burrfish-animal-spec-sheet.jpg" height="200"/>
  <img src="/assets/worm_like_pattern.png" width="200"/>
  <br>
  <b> Figure 5: Burrfish</b> (retrieved from <a href="https://scaquarium.org">South Carolina Aquarium</a>)
</p>

### Tiled FK Map
The following pattern represents the distribution of f and k parameters over x-y axes. We can exploit this map to re-create [mona lisa](https://github.com/Kashu7100/ComputationalArt/blob/master/assets/gray_scott_monalisa.png) with the Gray Scott model.

<p align="center">
  <img src="/assets/fk_map.png" width="300"/>
</p>
