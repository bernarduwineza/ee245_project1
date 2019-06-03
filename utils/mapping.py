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


def create_grid(data, res):
    """
        Returns a grid representation of a 3D configuration space
        based on given obstacle data.

        The `res` argument sets the resolution of the grid map.
    """

    # set grid size
    x_max, y_max, z_max = data[0, 0:3]

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
    print('Pickled the map...')
    return grid

def create_voxmap(data, voxel_size):
    """
    Returns a grid representation of a 3D configuration space
    based on given obstacle data.

    The `voxel_size` argument sets the resolution of the voxel map.
    """

    # minimum and maximum north coordinates
    north_min = np.floor(np.amin(data[:, 0] - data[:, 3]))
    north_max = np.ceil(np.amax(data[:, 0] + data[:, 3]))

    # minimum and maximum east coordinates
    east_min = np.floor(np.amin(data[:, 1] - data[:, 4]))
    east_max = np.ceil(np.amax(data[:, 1] + data[:, 4]))

    alt_max = np.ceil(np.amax(data[:, 2] + data[:, 5]))

    # given the minimum and maximum coordinates we can
    # calculate the size of the grid.
    north_size = int(np.ceil((north_max - north_min))) // voxel_size
    east_size = int(np.ceil((east_max - east_min))) // voxel_size
    alt_size = int(alt_max) // voxel_size

    voxmap = np.zeros((north_size, east_size, alt_size), dtype=np.bool)

    for i in range(data.shape[0]):
        north, east, alt, d_north, d_east, d_alt = data[i, :]
        # TODO: fill in the voxels that are part of an obstacle with `True`
        obstacles = [
            int(north - d_north - north_min) // voxel_size,
            int(north + d_north - north_min) // voxel_size,
            int(east - d_east - east_min) // voxel_size,
            int(east + d_east - east_min) // voxel_size,
        ]
        height = int(alt + d_alt) // voxel_size
        voxmap[obstacles[0]:obstacles[1], obstacles[2]:obstacles[3], 0:height] = True
        # i.e. grid[0:5, 20:26, 2:7] = True

    return voxmap


def visualise_voxmap(voxmap):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.voxels(voxmap, edgecolor='k')
    ax.set_xlim(voxmap.shape[0], 0)
    ax.set_ylim(0, voxmap.shape[1])
    # add 100 to the height so the buildings aren't so tall
    ax.set_zlim(0, voxmap.shape[2])

    plt.xlabel('X')
    plt.ylabel('Y')

    plt.show()


def create_local_voxmap(data, position, limits, voxel_size):
    """
    Returns a grid representation of a 3D configuration space
    based on given obstacle data.

    The `voxel_size` argument sets the resolution of the voxel map.
    """

    # minimum and maximum north coordinates
    north_min = np.floor(position[0] - limits)
    north_max = np.ceil(position[0] + limits)

    # minimum and maximum east coordinates
    east_min = np.floor(position[1] - limits)
    east_max = np.ceil(position[1] + limits)

    alt_max = np.ceil(position[2] + limits)

    # given the minimum and maximum coordinates we can
    # calculate the size of the grid.
    north_size = int(np.ceil((north_max - north_min))) // voxel_size
    east_size = int(np.ceil((east_max - east_min))) // voxel_size
    alt_size = int(alt_max) // voxel_size

    voxmap = np.zeros((north_size, east_size, alt_size), dtype=np.bool)

    for i in range(data.shape[0]):
        if np.array_equal(data[i], position):
            indx = i
            break
    north, east, alt, d_north, d_east, d_alt = data[indx - limits:indx + limits + 1, :]
    # TODO: fill in the voxels that are part of an obstacle with `True`
    obstacles = [
        int(north - d_north - north_min) // voxel_size,
        int(north + d_north - north_min) // voxel_size,
        int(east - d_east - east_min) // voxel_size,
        int(east + d_east - east_min) // voxel_size,
    ]
    height = int(alt + d_alt) // voxel_size
    voxmap[obstacles[0]:obstacles[1], obstacles[2]:obstacles[3], 0:height] = True
    # i.e. grid[0:5, 20:26, 2:7] = True

    return voxmap