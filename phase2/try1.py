import numpy as np
import io
import pickle
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

    filepath = 'SampleEnvironment.txt'
    s = open(filepath).read().replace(':', ';')

    # Assuming the obstacles begin after two lines as indicated in the sample file
    # It is also assumed that no line is blank after the second intentional blank line
    size = s.splitlines()[0]

    size = np.loadtxt(io.StringIO(size), delimiter=';', dtype='Float64', comments='#')

    data = np.loadtxt(io.StringIO(s), delimiter=';', dtype='Float64', comments='#', skiprows=2)

    obstacle_list=[]
    obstacle_exp = obstacle(location=[2, 2, 0], size=[10, 10, 10])
    obstacle_2 = obstacle(location=[8, 5, 2], size=[10, 2, 15])
    obstacle_list.append(obstacle_exp)
    obstacle_list.append(obstacle_2)

    for i in range(len(data)):
        new_obstacle = obstacle(location=data[i][0:3], size=data[i][3:5])
        obstacle_list.append(new_obstacle)
    size_map = [40, 40, 40]

    map = init_setting(end=(20, 20, 10))
    path = astar(map.maze, map.start, map.end)
    # print(path)
    path_pkl = open('./path2.pkl', 'wb')
    pickle.dump(path, path_pkl)
    path_pkl.close()
    print('Pickled the path...')

    draw_figure(obstacle_list, path, size_map)


if __name__ == '__main__':
    main()
