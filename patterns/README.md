## Overview


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

### self-replicating spots (f=0.022, k=0.05)
Hawaiian Whitespotted Toby
<p align="center">
  <img src="https://mauioceancenter.com/wp-content/uploads/2017/09/White-Spotted-Toby-web-1-768x512.jpg" height="180"/>
  <img src="https://github.com/Kashu7100/Recreation-of-Nature/blob/master/assets/self_replacing_spots.png" height="200"/>
</p>

### unstable spots (f=0.012, k=0.05)
<p align="center">
  <img src="https://github.com/Kashu7100/Recreation-of-Nature/blob/master/assets/unstable_spots.png" width="300"/>
</p>
