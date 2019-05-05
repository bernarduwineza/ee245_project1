"""
This is the main file of the Project
"""
import numpy as np
from trajectory import traj2D
from model.quadrotor import Quadrotor
from utils.quadPlot import plot_quad_3d
from utils import controller


def main():
    pos = (0, 0, 0)
    attitude = (0, 0, 0)

    vel = 2
    acc = 2.0
    iterations = 10
    waypoints = traj2D.vert_waypoints(0, 5)
    dt = 0.01
    drone = Quadrotor(pos, attitude)


    def loop(i):
        for k in range(len(waypoints)-1):
            state = traj2D.straight_line(np.array([0, 0, vel]), waypoints[k, :], waypoints[k+1, :])
            print (waypoints[k+1, :])
            f, m = controller.run(drone, state)
            drone.update(dt, f, m)
            wf = drone.world_frame()
            print (drone.position())
        print(str(i) + ": The drone's position is: " + str(drone.position()))
        return wf


    plot_quad_3d(waypoints, loop)


if __name__ == "__main__":
    main()
