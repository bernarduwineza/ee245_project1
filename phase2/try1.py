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
    obstacle_2 = obstacle(location=[8, 5, 2], size=[0, 4, 10])
    obstacle_list.append(obstacle_exp)
    obstacle_list.append(obstacle_2)
    size_map = [40, 40, 40]

    map = init_setting(end=(20, 20, 10))
    path = astar(map.maze, map.start, map.end)
    print(path)
    draw_figure(obstacle_list, path, size_map)


if __name__ == '__main__':
    main()
