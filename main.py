import utils
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation


def main():
    n_particles = 10
    box_size_x = 30
    box_size_y = 30
    elastic_constant = 1.0
    potential = None
    acceleration_vector = [0.0, -0.01]

    n_frames = 1000
    fig, ax = plt.subplots()

    position_limits_x = np.array([-box_size_x/2+box_size_x/10, box_size_x/2-box_size_x/10])
    position_limits_y = np.array([-box_size_y/2+box_size_y/10, box_size_y/2-box_size_y/10])
    velocity_limits_x = position_limits_x/100
    velocity_limits_y = position_limits_y/100


    x_init, y_init, v_x_init, v_y_init = utils.get_init_conditions(n_particles=n_particles, position_limits_x=position_limits_x, position_limits_y=position_limits_y, velocity_limits_x=velocity_limits_x, velocity_limits_y=velocity_limits_y)
    particles = utils.Particles(x_init, y_init, v_x_init, v_y_init, acceleration_vector[0], acceleration_vector[1])
    simulation = FuncAnimation(fig, utils.simulate, fargs=(particles, ax, box_size_x, box_size_y, elastic_constant), frames=n_frames, interval=25, repeat=False)
    #plt.legend()
    plt.show()


if __name__ == "__main__":
    main()