import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from function_planning  import Node
import function_planning
from function_planning import astar
import init_setting
from init_setting import init_setting



def main():
    obstacle_list=[]
    ## you finish the obstacle_list
    obstacle=obstacle(location=None, size=None)##
    obstacle_list.append(obstacle)
    ##
    map=init_setting(obstacle_loc=[2, 2, 0], obstacle_size=[10, 10, 10],end=(20, 20, 0))
    path = astar(map.maze, map.start, map.end)
    print(path)


if __name__ == '__main__':
    main()
