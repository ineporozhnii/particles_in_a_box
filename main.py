import utils
import random
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

def main():
    save = False
    np.random.seed(123)
   # plt.style.use("dark_background")
    matplotlib.rcParams['axes.linewidth'] = 3
    n_particles = 100
    box_size_x = 60
    box_size_y = 30
    restitution_coef_bc = 1.0
    restitution_coef_pc = 1.0
    potential = None
    acceleration_vector = [0.0, 0.0]

    n_frames = 1000
    fig, ax1 = plt.subplots(figsize=(box_size_x/5, box_size_y/5))

    radii_limits = np.array([0.3, 1.0])
    position_limits_x = np.array([-box_size_x/2+box_size_x/10, box_size_x/2-box_size_x/10])
    position_limits_y = np.array([-box_size_y/2+box_size_y/10, box_size_y/2-box_size_y/10])
    velocity_limits_x = position_limits_x/5
    velocity_limits_y = position_limits_y/5

    x_init, y_init, v_x_init, v_y_init, radii = utils.get_init_conditions(n_particles=n_particles, position_limits_x=position_limits_x, position_limits_y=position_limits_y, velocity_limits_x=velocity_limits_x, velocity_limits_y=velocity_limits_y, radii_limits=radii_limits)
    particles = utils.Particles(x_init, y_init, v_x_init, v_y_init, acceleration_vector[0], acceleration_vector[1], radii, vector_of_masses=np.pi*radii**2)
    simulation = FuncAnimation(fig, utils.simulate, fargs=(particles, ax1, box_size_x, box_size_y, restitution_coef_bc, restitution_coef_pc), frames=n_frames, interval=1, repeat=False)
    if save:
        Writer = animation.writers['ffmpeg']
        writer = Writer(fps=60, bitrate=8000)
        simulation.save('simulation.mp4', writer=writer)
    else:
        plt.show()


if __name__ == "__main__":
    main()