import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from function_planning  import Node
import function_planning
from function_planning import astar
import init_setting
from init_setting import init_setting
from init_setting import obstacle
from function_planning import draw_figure


def main():
    obstacle_list=[]
    obstacle_exp = obstacle(location=[2, 2, 0], size=[10, 10, 10])
    obstacle_list.append(obstacle_exp)

    map=init_setting(end=(20, 20, 0))
    path = astar(map.maze, map.start, map.end)
    print(path)
    draw_figure(obstacle_list, path)


if __name__ == '__main__':
    main()
