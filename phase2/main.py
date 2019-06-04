import numpy as np
import io
import pickle
import time
import cProfile
import re
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from function_planning  import Node
import function_planning
from function_planning import astar
import init_setting
from init_setting import init_setting
from init_setting import obstacle
from function_planning import draw_figure
import navigation2

def main():
    start_t = time.perf_counter()
    filepath = 'SampleEnvironment.txt'
    s = open(filepath).read().replace(':', ';')

    # Assuming the obstacles begin after two lines as indicated in the sample file
    # It is also assumed that no line is blank after the second intentional blank line
    size = s.splitlines()[0]

    size = np.loadtxt(io.StringIO(size), delimiter=';', dtype='Float64', comments='#')

    data = np.loadtxt(io.StringIO(s), delimiter=';', dtype='Float64', comments='#', skiprows=2)

    obstacle_list = []

    for i in range(len(data)):
        new_obstacle = obstacle(location=data[i][0:3], size=data[i][3:5])
        obstacle_list.append(new_obstacle)
    size_map = [40, 40, 40]

    map = init_setting(end=(20, 20, 10))
    path = astar(map.maze, map.start, map.end)
    # print(path)
    path_pkl = open('./path.pkl', 'wb')
    pickle.dump(path, path_pkl)
    path_pkl.close()
    print('Pickled the path...')

    end_t = time.perf_counter()
    elapsed_time = end_t - start_t
    draw_figure(obstacle_list, path, size_map)





    print('Done... in', elapsed_time, 'seconds')

    # use the path for navigation
    navigation2.navigation()
if __name__ == '__main__':
    main()

