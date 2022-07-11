import utils
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation


def main():
    matplotlib.rcParams['axes.linewidth'] = 3
    n_particles = 5
    box_size_x = 60
    box_size_y = 30
    restitution_coef_bc = 1.0
    restitution_coef_pc = 1.0
    potential = None
    acceleration_vector = [0.0, -1]

    n_frames = 1000
    fig, ax = plt.subplots(figsize=(box_size_x/5, box_size_y/5))

    position_limits_x = np.array([-box_size_x/2+box_size_x/10, box_size_x/2-box_size_x/10])
    position_limits_y = np.array([-box_size_y/2+box_size_y/10, box_size_y/2-box_size_y/10])
    velocity_limits_x = position_limits_x * 5
    velocity_limits_y = position_limits_y * 5


    x_init, y_init, v_x_init, v_y_init, radii = utils.get_init_conditions(n_particles=n_particles, position_limits_x=position_limits_x, position_limits_y=position_limits_y, velocity_limits_x=velocity_limits_x, velocity_limits_y=velocity_limits_y)
    particles = utils.Particles(x_init, y_init, v_x_init, v_y_init, acceleration_vector[0], acceleration_vector[1], radii, vector_of_masses=radii)
    simulation = FuncAnimation(fig, utils.simulate, fargs=(particles, ax, box_size_x, box_size_y, restitution_coef_bc), frames=n_frames, interval=1, repeat=False)
    plt.show()


if __name__ == "__main__":
    main()