# Simulation of particle mechanics 
In this project I created Python program that simulates particle mechanics including particle collisions and acceleration by external force.
<p align="center">
  <img src="https://github.com/ineporozhnii/Particles_in_the_box/blob/main/media/simulation_light.gif" alt="animated" />
</p>

# Implementation 
The simulation starts with assignment of initial conditions and parameters. The parameters that can be adjusted before simulation include: 
* Number of frames to simulate 
* Number of particles 
* Box size (width, height)
* Particle radii limits
* Particle initial position limits
* Particle initial velocity limits
* Restitution coefficient for particle-border collisions
* Restitution coefficient for particle-particle collision
* External acceleration vector  

Positions, velocities, and radii of all particles are stored as arrays in Particles() class. This allows us to avoid any explicit loops during the simulation and use the power of linear algebra, vectorization, and broadcasting. 


