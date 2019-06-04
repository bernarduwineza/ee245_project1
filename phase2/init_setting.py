import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from function_planning import obstacle


obstacle_list=[]
obstacle_exp=obstacle(location=[2, 2, 0],size=[10, 10, 10])
obstacle_list.append(obstacle_exp)
class init_setting():

    def __init__(self, figure_scale=40, gird_length=1, obstacles=obstacle_list,
                 start=(0, 0, 0), end=(20, 10, 0)):
        self.figure_scale=figure_scale
        self.gird_length=gird_length
        # self.obstacle_loc=obstacle_loc
        # self.obstacle_size=obstacle_size
        self.start=start
        self.end=end
        self.obstacles=obstacles
        figure_grid = int(figure_scale / gird_length)
        maze_zero = np.zeros((figure_grid, figure_grid, figure_grid))
        for i in range(len(obstacles)):
            obstacle_loc=obstacles[i].location
            obstacle_size=obstacles[i].size


            obstacle_size = [int(c / gird_length) for c in obstacle_size]  ##int(obstacle_size/gird_length)
            obstacle_loc = [int(c / gird_length) for c in obstacle_loc]  # int(obstacle_loc/gird_length)
            maze_zero[(obstacle_loc[0] ):(obstacle_loc[0] + obstacle_size[0] + 1),(obstacle_loc[1] ):(obstacle_loc[1] + obstacle_size[1] + 1),(obstacle_loc[2] ):(obstacle_loc[2] + obstacle_size[2] + 1)] = 1


        self.maze = maze_zero
        if self.maze[end[0], end[1], end[2]] is 1:
            print('fault')


