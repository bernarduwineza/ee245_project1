import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""
    ##draw the picture

    fig3 = plt.figure(3)
    ax_3d = Axes3D(fig3)
    pos_text = ax_3d.text2D(0.05, 0.8, '', transform=ax_3d.transAxes)
    pos_template = 'Current position = (%.2f,%.2f，%.2f)'
    ax_3d.set_xlim3d(0, 40)
    ax_3d.set_ylim3d(0, 40)
    ax_3d.set_zlim3d(0, 40)
    plt.ion()
    plt.title('The path of the Quadrotor in 3D')
    ax_3d.set_xlabel('X-axis')
    ax_3d.set_ylabel('Y-axis')
    ax_3d.set_zlabel('Z-axis')
    C_obs = ax_3d.bar3d(2, 2, 0, 10,
                        10, 10)

    # Create start and end node
    start_node = Node(None, start)
    # start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    # end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]##output the object
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index


        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)
        print(current_node.position)

        ## draw the point
        # ax_3d.scatter(current_node.position[0], current_node.position[1], current_node.position[2], c='r', marker=".")
        ax_3d.scatter(current_node.position[0], current_node.position[1], current_node.position[2])
        pos_text.set_text(pos_template % (current_node.position[0], current_node.position[1], current_node.position[2]))
        # ax_3d.draw()  # 注意此函数需要调用

        plt.show()
        plt.pause(0.001)
        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, 0, -1), (0, 0, 1), (-1, 0, 0), (1, 0, 0), (0, -1, 0 ), (0, 1, 0)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1], current_node.position[2] + new_position[2])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0 \
                    or node_position[2] > maze.shape[2]-1 or node_position[2] < 0 :
                continue
            # if node_position is current_node.parent:
            #     continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]][node_position[2]] != 0:
                print(node_position)
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:
            a=0
            b=0
            # Child is on the closed list
            for closed_child in closed_list:
                if child.position[0] == closed_child.position[0] and child.position[1] == closed_child.position[1] and child.position[2] == closed_child.position[2] :
                    a=1
                    break
            if a==1:
                continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2) + ((child.position[2] - end_node.position[2]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node: #and child.g > open_node.g:
                    b=1
                    break
            if b == 1:
                continue

            # Add the child to the open list
            open_list.append(child)
            print('fuccccccadd:%d',child.position)


def main():
    figure_scale = 40
    gird_length = 1


    figure_grid=int(figure_scale/gird_length)
    maze_zero = np.zeros((figure_grid , figure_grid , figure_grid))
    start = (0, 0, 0)
    end=(20,20,0)
    #end = (int(50), int(50), int(50))
    #end=[int(c) for c in end]
    obstacle_size = [10, 10, 10]
    obstacle_loc = [2, 2, 0]
    obstacle_size=[int(c/gird_length) for c in obstacle_size]##int(obstacle_size/gird_length)
    obstacle_loc = [int(c/gird_length) for c in obstacle_loc]#int(obstacle_loc/gird_length)
    #maze_zero[obstacle_loc[0]:obstacle_loc[0] + obstacle_size[0], obstacle_loc[1]:obstacle_loc[1] + obstacle_size[1], obstacle_loc[2]:obstacle_loc[2] + obstacle_size[2]] = np.ones((obstacle_size[0], obstacle_size[1], obstacle_size[2]))
    maze_zero[(obstacle_loc[0]-1):(obstacle_loc[0] + obstacle_size[0]+1), (obstacle_loc[1]-1):(obstacle_loc[1] + obstacle_size[1]+1), (obstacle_loc[2]-1):(obstacle_loc[2] + obstacle_size[2]+1)] = 1
    maze_zero[1:12,1:12,0:10]=1
    maze=maze_zero
    if maze[end[0], end[1], end[2]] is 1:
        print('fault')
        return

    path = astar(maze, start, end)
    print(path)


if __name__ == '__main__':
    main()
