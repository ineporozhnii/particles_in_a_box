# Simulation of particle mechanics 
In this project I created Python program that simulates particle mechanics including particle collisions and acceleration by external force.
<p align="center">
  <img src="https://github.com/ineporozhnii/Particles_in_the_box/blob/main/media/simulation_light.gif" alt="animated" />
</p>

# Implementation 
The simulation starts with assignment of initial conditions and parameters. The parameters that can be adjusted include: 
* Number of frames to simulate 
* Number of particles 
* Box size (width, height)
* Particle radii limits
* Particle initial position limits
* Particle initial velocity limits
* Restitution coefficient for particle-border collisions
* Restitution coefficient for particle-particle collisions
* External acceleration vector  

Positions, velocities, and radii of all particles are stored as arrays in Particles() class. This allows us to avoid any explicit loops during the simulation and use the power of linear algebra, vectorization, and broadcasting. At each simulation frame, the distance matrix between all particles is calculated and colliding particle pairs are detected. The velocities of particle pairs after the collision are calculated using following equations:

$$ \mathbf{v_1'} = \mathbf{v_1} - {{(C_r + 1) m_2 } \over {m_1 + m_2}} {\langle {\mathbf{v_1} - \mathbf{v_2}}, {\mathbf{x_1} - \mathbf{x_2}}\rangle \over {|| \mathbf{x_1} - \mathbf{x_2} ||^2}} (\mathbf{x_1} - \mathbf{x_2})$$

$$ \mathbf{v_2'} = \mathbf{v_2} - {{(C_r + 1) m_1 } \over {m_1 + m_2}} {\langle {\mathbf{v_2} - \mathbf{v_1}}, {\mathbf{x_2} - \mathbf{x_1}}\rangle \over {|| \mathbf{x_2} - \mathbf{x_1} ||^2}} (\mathbf{x_2} - \mathbf{x_1})$$

Where $\mathbf{v_1'}$ and $\mathbf{v_2'}$ - velocity vectors after the collision, $\mathbf{v_1}$ and $\mathbf{v_2}$ - velocity vectors before the collision, $\mathbf{x_2}$ and $\mathbf{x_1}$ - position vectors, $m_1$ and $m_2$ - particle masses, $C_r$ - restitution coefficient for particle-particle collisions. $\langle \ , \rangle$ indicate the dot product of two vectors.

By changing restitution coefficients for particle-particle and particle-border collisions we can compare systems with elastic ($C_r = 1$) and inelastic ($C_r < 1$) collisions.

<p align="center">
  <img src="https://github.com/ineporozhnii/Particles_in_the_box/blob/main/media/restitution_coef_comparison.gif" alt="animated" />
</p>

We can also define an acceleration vector that simulates an external force. 

<p align="center">
  <img src="https://github.com/ineporozhnii/Particles_in_the_box/blob/main/media/acceleration_vector_comparison.gif" alt="animated" />
</p>
