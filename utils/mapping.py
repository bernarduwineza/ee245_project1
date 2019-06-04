"""
Environment and obstacle mapping using binary occupancy grids.
Given a certain representation of obstacles, map them into a robot configuration space.
The obstacles are 3-dimensional rectangular parallelepiped objects, represented by their origins, and length of sides.
    An obstacles is represented by 6 real numbers (3: origin, 3: length of x,y,z sides)

The  map is a rectangular parallelepiped coonfiguration space specified by its side lengths.
"""

# coding: utf-8

# # 3D Map
#
# While representing the configuration space in 3 dimensions isn't entirely practical it's fun (and useful) to visualize things in 3D.
#
# In this exercise you'll finish the implementation of `create_grid` such that a 3D grid is returned where cells containing a voxel are set to `True`. We'll then plot the result!

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
import pickle


def create_grid(data, res, size):
    """
        Returns a grid representation of a 3D configuration space
        based on given obstacle data.

        The `res` argument sets the resolution of the grid map.
    """

    # set grid size
    x_max, y_max, z_max = size

    x_size = int(x_max // res)
    y_size = int(y_max // res)
    z_size = int(z_max // res)

    grid = np.zeros((x_size, y_size, z_size), dtype=np.int)

    start = time.perf_counter()
    for i in range(data.shape[0]-1):

        x, y, z, dx, dy, dz = data[i+1, :]
        # TODO: fill in the voxels that are part of an obstacle with `True`
        obstacles = [
            int(x // res),
            int(x + dx // res),

            int(y // res),
            int(y + dy // res),

            int(z // res),
            int(z + dz // res)
        ]
        grid[obstacles[0]:obstacles[1], obstacles[2]:obstacles[3], obstacles[4]:obstacles[5]] = 1
    end = time.perf_counter()
    print('Finished generating map in: ', str(end-start), 'seconds \n')
    print('Number of grids: ', str(x_size*y_size*z_size), 'cells \n')

    grid_pkl = open('grid.pkl', 'wb')
    pickle.dump(grid, grid_pkl)
    grid_pkl.close()
    print('Pickled the grid map...')
    return grid

def visualise_grid(grid):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.voxels(grid, edgecolor='k')
    ax.set_xlim(grid.shape[0], 0)
    ax.set_ylim(0, grid.shape[1])
    # add 100 to the height so the buildings aren't so tall
    ax.set_zlim(0, grid.shape[2])

    plt.xlabel('X')
    plt.ylabel('Y')

    plt.show()
