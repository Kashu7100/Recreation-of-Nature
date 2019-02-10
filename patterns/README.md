## Overview


## Gray Scott Model of Reaction Diffusion

Gray Scott model describes the variation of u and v, which represent the concentration of chemical U and V respectively. U and V react according the following equation:

<center><img src="https://latex.codecogs.com/gif.latex?U&plus;2V\rightarrow&space;3V" title="U+2V\rightarrow 3V" /></center>

<a href="https://www.codecogs.com/eqnedit.php?latex=V\rightarrow&space;P" target="_blank"><img src="https://latex.codecogs.com/gif.latex?V\rightarrow&space;P" title="V\rightarrow P" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;u}{\partial&space;t}&space;=&space;D_u\triangledown^2u&space;-&space;uv^2&space;&plus;&space;F(1-u)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;u}{\partial&space;t}&space;=&space;D_u\triangledown^2u&space;-&space;uv^2&space;&plus;&space;F(1-u)" title="\frac{\partial u}{\partial t} = D_u\triangledown^2 - uv^2 + F(1-u)" /></a>

<a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;v}{\partial&space;t}&space;=&space;D_v\triangledown^2v&space;-&space;uv^2&space;-&space;(F&plus;k)v" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{\partial&space;v}{\partial&space;t}&space;=&space;D_v\triangledown^2v&space;+&space;uv^2&space;-&space;(F&plus;k)v" title="\frac{\partial v}{\partial t} = D_v\triangledown^2v - uv^2 - (F+k)v" /></a>

This model can be seen as a simulation of the behavior of diffusive living things reproducing under conditions of limited food. Different patterns emerge for slight changes in feeding and death rates.

### unstable spots (f=0.012, k=0.05)
<p align="center">
  <img src="https://github.com/Kashu7100/Recreation-of-Nature/blob/master/assets/unstable_spots.gif" width="300"/>
</p>
