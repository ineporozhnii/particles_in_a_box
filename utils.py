import numpy as np

class Particles():
    """
    This class holds particle positions, velocities, accelerations, and properties
    """
    def __init__(self, x, y, v_x, v_y, a_x, a_y) -> None:
        self.radii = 5
        self.colors = "cornflowerblue"
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        self.a_x = a_x
        self.a_y = a_y


def get_init_conditions(n_particles, position_limits_x, position_limits_y, velocity_limits_x, velocity_limits_y):
    """
    This function creates initial distribution of particle positions and velocities
    Input:
        n_atoms - number of atoms in the simulations
        position_limits_x - list of low and high limits for initial atomic positions on x axis
        position_limits_y - list of low and high limits for initial atomic positions on y axis
        velocity_limits_x - list of low and high limits for initial atomic velocities on x axis
        velocity_limits_y - list of low and high limits for initial atomic velocities on y axis
    Output:
        x_init - initial x coordinates 
        y_init - initial y coordinates 
        v_x_init - initial x velocities 
        v_y_init - initial y velocities 
    """
    x_init = np.random.uniform(low=position_limits_x[0], high=position_limits_x[1], size=(n_particles,))
    y_init = np.random.uniform(low=position_limits_y[0], high=position_limits_y[1], size=(n_particles,))
    v_x_init = np.random.uniform(low=velocity_limits_x[0], high=velocity_limits_x[1], size=(n_particles,))
    v_y_init = np.random.uniform(low=velocity_limits_y[0], high=velocity_limits_y[1], size=(n_particles,))
    return x_init, y_init, v_x_init, v_y_init


def update_positions(x, y, v_x, v_y):
    x_new = x + v_x
    y_new = y + v_y
    return x_new, y_new


def simulate(frame_idx, particles, ax, box_size_x, box_size_y, elastic_constant):
    x_new, y_new = update_positions(particles.x, particles.y, particles.v_x, particles.v_y)
    # Add acceleration 
    if frame_idx%2 != 0:
        accelerate(particles)
    # Box boundary collisions
    particles.v_x[np.where(x_new > box_size_x/2)] = -1 * elastic_constant * particles.v_x[np.where(x_new > box_size_x/2)]
    particles.v_x[np.where(x_new < -box_size_x/2)] = -1 * elastic_constant * particles.v_x[np.where(x_new < -box_size_x/2)]
    particles.v_y[np.where(y_new > box_size_y/2)] = -1 * elastic_constant * particles.v_y[np.where(y_new > box_size_y/2)]
    particles.v_y[np.where(y_new < -box_size_y/2)] = -1 * elastic_constant * particles.v_y[np.where(y_new < -box_size_y/2)]
    x_new[np.where(x_new > box_size_x/2)] = box_size_x/2
    x_new[np.where(x_new < -box_size_x/2)] = -box_size_x/2
    y_new[np.where(y_new > box_size_y/2)] = box_size_y/2
    y_new[np.where(y_new < -box_size_y/2)] = -box_size_y/2
    # Update particle positions
    particles.x = x_new
    particles.y = y_new
    # Add acceleration 
    if frame_idx%2 == 0:
        accelerate(particles)
    # Calculate velocities
    velocities = np.sqrt(particles.v_x**2 + particles.v_y**2)
    # Plot particles
    ax.clear()
    ax.scatter(particles.x, particles.y, s=100, c=velocities, cmap='viridis', label = f"Average velocity {np.mean(velocities)}")
    ax.set_xlim([-box_size_x/2, box_size_x/2])
    ax.set_ylim([-box_size_y/2, box_size_y/2])
    print(f"Average velocity {np.mean(velocities)}")


def accelerate(particles):
    particles.v_x = particles.v_x + particles.a_x
    particles.v_y = particles.v_y + particles.a_y
