import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from function_planning  import Node
import function_planning
from function_planning import astar
import init_setting
from init_setting import init_setting



def main():
    map=init_setting(end=(20, 20, 0))


    path = astar(map.maze, map.start, map.end)
    print(path)


if __name__ == '__main__':
    main()
