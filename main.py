import utils
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation


def animate(i, atom, ax, box_size_x, box_size_y):
    x_new, y_new = utils.update_positions(atom.x, atom.y, atom.v_x, atom.v_y)
    atom.x = x_new
    atom.y = y_new
    # Box boundary collisions
    atom.v_x[np.where(x_new > box_size_x/2)] = -1 * atom.v_x[np.where(x_new > box_size_x/2)]
    atom.v_x[np.where(x_new < -box_size_x/2)] = -1 * atom.v_x[np.where(x_new < -box_size_x/2)]
    atom.v_y[np.where(y_new > box_size_y/2)] = -1 * atom.v_y[np.where(y_new > box_size_y/2)]
    atom.v_y[np.where(y_new < -box_size_y/2)] = -1 * atom.v_y[np.where(y_new < -box_size_y/2)]
    velocities = np.sqrt(atom.v_x**2 + atom.v_y**2)
    norm = plt.Normalize(velocities.min(), velocities.max())

    ax.clear()
    ax.scatter(atom.x, atom.y, c=velocities, cmap='viridis', s=10/velocities)
    ax.set_xlim([-box_size_x/2, box_size_x/2])
    ax.set_ylim([-box_size_y/2, box_size_y/2])


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
    ani = FuncAnimation(fig, animate, fargs=(atoms, ax, box_size_x, box_size_y), frames=500, interval=25, repeat=False)
    plt.show()


if __name__ == "__main__":
    main()