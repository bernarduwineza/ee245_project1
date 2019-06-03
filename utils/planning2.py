import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
import pickle


pkl_file = open('./../phase2/grid.pkl', 'rb')
grid = pickle.load(pkl_file)
pkl_file.close()

xdim = grid.shape[0]
ydim = grid.shape[1]
zdim = grid.shape[2]

delta = [[-1, 0, 0],  # zurück
         [0, -1, 0],  # links
         [1, 0, 0],  # vor
         [0, 1, 0],  # rechts
         [0, 0, -1],  # unten
         [0, 0, 1]]  # oben
cost = 1

heuristic = np.empty((xdim, ydim, zdim), dtype=np.float32)
heuristic[:] = 0.0


# A* Algorithm
# Based on the great Course CS373 from Udacity taught by Sebastian Thrun
# https://www.udacity.com/course/cs373
def search(init, goal, grid, heuristic, maxp):
    x = np.int(init[0])
    y = np.int(init[1])
    z = np.int(init[2])

    closed = np.empty((xdim, ydim, zdim), dtype=np.int8)
    closed[:] = 0
    closed[x, y, z] = 1

    expand = np.empty((xdim, ydim, zdim), dtype=np.int8)
    expand[:] = -1
    action = np.empty((xdim, ydim, zdim), dtype=np.int8)
    action[:] = -1

    g = 0
    h = heuristic[x, y, z]
    f = g + h

    openl = [[f, g, x, y, z]]

    found = False  # flag that is set when search is complete
    resign = False  # flag set if we can't find expand
    count = 0

    while not found and not resign and count < 1e6:
        if len(openl) == 0:
            resign = True
            return "Fail: Open List is empty"
        else:
            openl.sort()
            openl.reverse()
            nextl = openl.pop()

            x = nextl[2]
            y = nextl[3]
            z = nextl[4]
            g = nextl[1]
            f = nextl[0]
            expand[x, y, z] = count
            count += 1

            if x == goal[0] and y == goal[1] and z == goal[2]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    z2 = z + delta[i][2]

                    if z2 >= 0 and z2 < zdim and \
                            0 <= y2 < ydim and \
                            0 <= x2 < xdim:

                        if closed[x2, y2, z2] == 0 and grid[x2, y2, z2] < maxp:
                            g2 = g + cost
                            f2 = g2 + heuristic[x2, y2, z2]
                            openl.append([f2, g2, x2, y2, z2])
                            closed[x2, y2, z2] = 1

                            # Memorize the sucessfull action for path planning
                            action[x2, y2, z2] = i
                    else:
                        pass

    # print('\nA* Result:')
    # for i in range(len(expand)):
    #    print(expand[i])

    # Policy
    '''
    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    x = goal[0]
    y = goal[1]
    policy[x][y]='*' # Goal
    '''
    path = [[goal[0], goal[1], goal[2]]]

    while x != init[0] or y != init[1] or z != init[2]:
        x2 = x - delta[action[x, y, z]][0]
        y2 = y - delta[action[x, y, z]][1]
        z2 = z - delta[action[x, y, z]][2]
        # policy[x2][y2][z2]=delta_name[action[x][y][z]]
        x = x2
        y = y2
        z = z2
        # Path
        path.append([x2, y2, z2])

    '''
    print('\nActions:')
    for i in range(len(action)):
        print(action[i])

    print('\nPolicy (Path):')
    for i in range(len(policy)):
        print(policy[i])
    '''
    # print('\nCoordinates for Path smoothing=')
    path.reverse()

    '''
    for i in range(len(path)):
        print(path[i])
    '''
    return path


def calcheuristic(grid, goal):
    for z in range(zdim):
        for y in range(ydim):
            for x in range(xdim):
                # Euklidische Distanz für jede Zelle zum Ziel berechnen
                dist = ((x - goal[0]) ** 2 + (y - goal[1]) ** 2 + (z - goal[2]) ** 2) ** (1 / 2.0)

                # Höhe
                zheu = -6.0 * float(z)

                # Horizontale von Soll
                yheu = np.abs(float(y) - goal[1])

                # und Höhe und Abweichung von y=0
                heuristic[x, y, z] = dist + yheu  # + zheu
    '''     
    for i in range(len(heuristic)):
        print(heuristic[i])
    '''
    return heuristic


def smooth(path, weight_data=0.5, weight_smooth=0.2, tolerance=0.00001):
    # Make a deep copy of path into newpath
    newpath = [[0 for row in range(len(path[0]))] for col in range(len(path))]
    for i in range(len(path)):
        for j in range(len(path[0])):
            newpath[i][j] = path[i][j]

    change = tolerance
    while change >= tolerance:
        change = 0.0
        for i in range(1, len(path) - 1):  # 1. und letzten Punkt unberuhrt lassen
            for j in range(len(path[0])):
                aux = newpath[i][j]
                newpath[i][j] += weight_data * (path[i][j] - newpath[i][j])
                newpath[i][j] += weight_smooth * (newpath[i - 1][j] \
                                                  + newpath[i + 1][j] - (2.0 * newpath[i][j]))
                change += abs(aux - newpath[i][j])

    print('\nSmoothed Path')
    for i in range(len(path)):
        print(path[i], newpath[i])

    return newpath


start = [1.0, 1.0, 1.0]
goal = [15.0, 20, 30]

heuristic = calcheuristic(grid, goal)

maxp = 4.0
start_time = time.perf_counter()
path = search(start, goal, grid, heuristic, maxp)
end_time = time.perf_counter()

path_pkl = open('./../phase2/path.pkl', 'wb')
pickle.dump(path, path_pkl)
path_pkl.close()
print('Pickled the path...')

print('A* execution time is: ', str(end_time-start_time), 'seconds \n')

def plot3Dgrid(grid, az, el):
    # plot the surface
    plt3d = plt.figure()
    ax = plt3d.add_subplot(111, projection='3d')

    # create x,y
    ll, bb = np.meshgrid(range(grid.shape[1]), range(grid.shape[0]))

    for z in range(grid.shape[2]):
        if not (np.max(grid[:, :, z]) == np.min(grid[:, :, z])):  # unberührte Ebenen nicht darstellen
            cp = ax.contourf(ll, bb, grid[:, :, z], offset=z, alpha=0.3, cmap=plt.get_cmap('Greens'))

    cbar = plt.colorbar(cp, shrink=0.7, aspect=20)
    # cbar.ax.set_ylabel('$P(m|z,x)$')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim3d(0, grid.shape[0])
    ax.set_ylim3d(0, grid.shape[1])
    ax.set_zlim3d(0, grid.shape[2])
    # plt3d.axis('equal')
    ax.view_init(az, el)
    return ax


plt3d = plot3Dgrid(grid, 45, -115)
for p in path:
    plt3d.scatter(p[0], p[1], p[2], s=20, c='k')

plt.show()