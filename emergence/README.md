## Overview

## [Primordial Particle Systems (PPS)](https://www.nature.com/articles/srep37969)

<p align="center">
  <img src="https://github.com/Kashu7100/Recreation-of-Nature/blob/master/assets/pps.gif" width="500"/>
</p>

The motion law of PPS is described as following:

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=\frac{\Delta\Phi}{\Delta t} = \alpha %2B \beta \cdot N_{t,r} \cdot \sign(R_{t,r}-L_{t,r})">
</p>

where a positive change of <img src="https://render.githubusercontent.com/render/math?math=\Phi"> is a turn to the right. The parameter <img src="https://render.githubusercontent.com/render/math?math=\alpha"> represents a fixed rotation, <img src="https://render.githubusercontent.com/render/math?math=\beta"> models a rotation proportional to local neighborhood size. Neighborhood configuration affects <img src="https://render.githubusercontent.com/render/math?math=\Phi_t"> in each time step, in turn changing a particle’s position, ultimately yielding new local configurations. This feedback loop governs the self-organization of the PPS system.

Each particle holds position <img src="https://render.githubusercontent.com/render/math?math=p_t=(x_t,y_t)"> and heading <img src="https://render.githubusercontent.com/render/math?math=\Phi_t"> at every time step t. 

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=p_{t %2B 1} = p_t %2B (v_t \cos(\Phi_t), v_t \sin(\Phi_t))">
</p>

## [Substrate Catalyst Link (SCL)](https://www.sciencedirect.com/science/article/abs/pii/0303264774900318?via%3Dihub)

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=2S %2B C \rightarrow L %2B C">
</p>

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=L %2B L \rightarrow  BL">
</p>

<p align="center">
<img src="https://render.githubusercontent.com/render/math?math=L \rightarrow 2S">
</p>

## References
https://www.researchgate.net/publication/23319484_Shapes_and_Self-Movement_in_Protocell_Systems