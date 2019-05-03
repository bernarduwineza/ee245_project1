"""
This file defines the kinematic and dynamic model of the quadrotor

"""
import numpy as np
import  scipy.integrate as integrate


class Quadrotor:
    """
    state       - A 13x1 vector containing [x, y, z, xd, yd, zd, qw, qx, qy, qz, p, q, r]  where
                    x, y, z:    position
                    xd, yd, zd: linear velocities
                    qw, qx, qy, qz: quaternions
                    p, q, r:    angular velocities [roll, pictch, yaw]
    F           - scalar Thrust provided by the controller
    M           - 3x1 Moment vector supplied by the controller
    """

    def __init__(self, pos, attitude):
        """
        :param pos: [x,y,z]
        :param attitude: [roll, pitch, yaw]
        :return:
        """
        self.state = np.zeros(13)
        roll, pitch, yaw = attitude
        #TODO

    def world_frame(self):
        """

        :return: world_frame
        """

        #TODO


