<p align="center">
  <img src="https://github.com/Kashu7100/Recreation-of-Nature/blob/master/assets/swarm.png?raw=true" height="450"/>
</p>

## Overview

This section will get into the emergent phenomenon in group behavior. 

## Boids Model

Boids is an artificial life program, developed by [Craig Reynolds](http://www.red3d.com/cwr/index.html) in 1986, which simulates the flocking behaviour of birds. Boids stands for "bird-oids". The basic model consists of three simple steering behaviors which describe how an individual agent maneuvers based on the positions and velocities of sarrownding agents. 

| Cohesion | Separation | Alignment |
| ---- | ---- | ---- |
|<p align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/2/2b/Rule_cohesion.gif"/></p>|<p align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/e/e1/Rule_separation.gif"/></p>|<p align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/e/e1/Rule_alignment.gif"/></p>|
|move towards center of mass of the group|avoid collision with other members|face towards the average heading of the group|

Each agent can access directly to the whole scene's geometric description, but an agent is only affected by flockmates within a certain small neighborhood around itself.

### predator and prey

In the following simulation of predation, we can see a simulated interaction of predator and prey; one kills and eats another organism, where the predator is represented by the red arrow and the prey is represented by the blue arrow. 

[full video](https://www.youtube.com/watch?v=ITv39Q1UePA)

[source](/swarm/predator_prey.py)

<p align="center">
  <img src="https://github.com/Kashu7100/Recreation-of-Nature/blob/master/assets/boids_predator_prey.gif"/>
</p>


