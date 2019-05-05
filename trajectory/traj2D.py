"""
- This file describes the mechanisms for generating a 2D trajectory for the quadrotor.
- The quadrotor accelerates from an initial position to a hover position on the z-axis
    through a straight line
"""
# TODO:  Implement the trajectory generation --
# For now, just a straight vertical line followed by another line,
#   then a vertical line for landing.

from collections import namedtuple
import numpy as np


def vertical_hover(t):
    """
    Hover on the z-axis
    :param t: time to get there
    :return: position (pos), velocity (vel), acceleration (acc), yaw(yaw), yawdot
    """

    # define maximum acceleration and velocity
    v_max = 2.0
    a_max = 2.0
    yaw = 0.0
    yawdot = 0.0

    init_pos = np.zeros(3)
    acc = np.zeros(3)
    vel = np.zeros(3)

    # acceleration
    if t <= v_max/a_max:
        dt = t
        acc[2] = a_max
        vel = acc * dt
        pos = 0.5 * acc * dt**2

    # constant velocity
    elif t <= 2 * v_max / a_max:
        dt = t - v_max / a_max
        vel[2] = v_max
        pos = np.array([0, 0, (v_max**2 / (2 * a_max)) + (v_max * dt)])

    # slow down
    # TODO Test the acceleration, deceleration sequences
    elif t <= 3 * v_max / a_max:
        dt = t - 2 * v_max / a_max
        acc[2] = -a_max
        vel = np.array([0, 0, v_max]) + acc * dt
        pos = np.array([0, 0, (3 * v_max**2 / (2 * a_max)) + ((v_max * dt) + (0.5 * acc * dt**2))])

    # hover
    else:
        pos = np.array([0, 0, 2*v_max**2 / a_max])

    pos = init_pos + pos
    FinalState = namedtuple('FinalState', 'pos vel acc yaw yawdot')

    return FinalState(pos, vel, acc, yaw, yawdot)


def straight_line(vel, init_pos, final_pos):
    """
    A straight line in the yz- plane.  Done in constant velocity.
    :param vel: velocity
    :param init_pos: initial position
    :param final_pos: final position
    :return: position (pos), velocity (vel), acceleration (acc), yaw(yaw), yawdot
    """

    acc = np.zeros (3)
    yaw = 1.0
    yawdot = 1.0

    p = (final_pos[2] - init_pos[2])/vel [2]
    #acc = (final_pos[2] - init_pos[2])/dt ** 2

    # constant velocity
    pos = init_pos + np.array([0, 0, p])
    FinalState = namedtuple('FinalState', 'pos vel acc yaw yawdot')
    return FinalState(pos, vel, acc, yaw, yawdot)

def vert_waypoints(t, n):
    """
    :param t: time to get there
    :param n: number of points
    :return: positions of the waypoints
    """
    waypoints = np.linspace(t, t + 2*np.pi, n)
    x = waypoints * 0
    y = waypoints * 0
    z = waypoints

    return np.stack((x, y, z), axis=-1)

