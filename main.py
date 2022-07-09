import utils
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation


def main():
    n_atoms = 10
    box_size_x = 30
    box_size_y = 30
    potential = None
    fig, ax = plt.subplots()

    position_limits_x = np.array([-box_size_x/2+box_size_x/10, box_size_x/2-box_size_x/10])
    position_limits_y = np.array([-box_size_y/2+box_size_y/10, box_size_y/2-box_size_y/10])
    velocity_limits_x = position_limits_x/10
    velocity_limits_y = position_limits_y/10

    x_init, y_init, v_x_init, v_y_init = utils.get_init_conditions(n_atoms=n_atoms, position_limits_x=position_limits_x, position_limits_y=position_limits_y, velocity_limits_x=velocity_limits_x, velocity_limits_y=velocity_limits_y)
    atoms = utils.Atoms(x_init, y_init, v_x_init, v_y_init)
    ani = FuncAnimation(fig, utils.animate, fargs=(atoms, ax, box_size_x, box_size_y), frames=500, interval=25, repeat=False)
    plt.show()


if __name__ == "__main__":
    main()