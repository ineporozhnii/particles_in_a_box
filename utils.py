import numpy as np

class Atoms():
    """
    This class is used to hold atom positions and properties
    """
    def __init__(self, x, y, v_x, v_y) -> None:
        self.radii = 5
        self.colors = "cornflowerblue"
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y

def get_init_conditions(n_atoms, position_limits_x, position_limits_y, velocity_limits_x, velocity_limits_y):
    """
    This function creates initial distribution of atomic positions and velocities
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
    x_init = np.random.uniform(low=position_limits_x[0], high=position_limits_x[1], size=(n_atoms,))
    y_init = np.random.uniform(low=position_limits_y[0], high=position_limits_y[1], size=(n_atoms,))
    v_x_init = np.random.uniform(low=velocity_limits_x[0], high=velocity_limits_x[1], size=(n_atoms,))
    v_y_init = np.random.uniform(low=velocity_limits_y[0], high=velocity_limits_y[1], size=(n_atoms,))
    return x_init, y_init, v_x_init, v_y_init

def update_positions(x, y, v_x, v_y):
    x_new = x + v_x
    y_new = y + v_y
    return x_new, y_new

