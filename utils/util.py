"""
The model of the quadrotor

authors: Jean-bernard Uwineza & Zhao Hangquan
"""
import numpy as np
from scipy import integrate
from utils import params
g = params.g


class Controller:

    @staticmethod
    def control_2d(q0, qh, zt, T):
        """

        :param q0: initial pose
        :param qh: hover pose
        :param zt: height of hovering on the z-axis
        :param T: time hovering
        :return: 2D pose and time differential
        """

        kd = 2.0
        kp = 1
        dt = .01

        # vertical takeoff on the z-axis
        p_zt = np.array([q0[0],[zt]])
        X1 = Model.dynamic_2d(q0, p_zt, kd, kp)

        #s traight line
        p_l = X1[:2, -1].reshape(2,1)
        X2 = Model.dynamic_2d(p_l, qh, kd, kp)

        # hover
        X3 = Maneuver.hover(X2[:,-1], T, dt)

        # vertical landing on the z-axis
        p_land = np.array([qh[0], [0.0]])
        p_zl = X3[:2,-1].reshape(2,1)
        X4 = Model.dynamic_2d(p_zl, p_land, kd, kp)
        X_2d = np.concatenate((X1, X2, X3, X4), axis=1)

        return X_2d, dt

    @staticmethod
    def control_3d(q0, qh, zt, T):
        """

        :param q0: initial pose
        :param qh: hover pose
        :param zt: height of hovering on the z-axis
        :param T: time hovering
        :return: 3D pose and time differential
        """
        kd = 3.0
        kp = 2
        dt = .01

        # vertical takeoff on the z-axis
        p_zt = np.array([q0[0], q0[1], [zt]])
        X1 = Model.dynamic_3d(q0, p_zt, kd, kp)

        # straight line
        p_l = X1[:3, -1].reshape(3, 1)
        X2 = Model.dynamic_3d(p_l, qh, kd, kp)

        # hover
        X3 = Maneuver.hover(X2[:, -1], T, dt)

        # vertical landing on the z-axis
        p_land = np.array([qh[0], qh[1], [0.0]])
        p_zl = X3[:3, -1].reshape(3, 1)
        X4 = Model.dynamic_3d(p_zl, p_land, kd, kp)
        X_3d = np.concatenate((X1, X2, X3, X4), axis=1)

        return X_3d, dt

    @staticmethod
    def control(q0, qf):
        kd = 3.0
        kp = 2
        dt = .01



class Model:

    @staticmethod
    def dynamic_2d(p0, pf, kd, kp):
        """

        :param p0: initial pose
        :param pf: final pose
        :param kd: control gain
        :param kp: control gain
        :return: 2D pose
        """
        g = 9.81

        # displacement and its norm
        dp = pf - p0
        d = np.linalg.norm(dp)
        dp = dp.reshape(dp.shape[0])
        state = PD(kd, kp, 0.0, 0.0, d)

        p = state[:, 0]
        v = state[:, 1]

        p = p.reshape(1, p.shape[0])
        v = v.reshape(1, v.shape[0])

        py = p0[0] + p*dp[0]/d
        pz = p0[1] + p*dp[1]/d
        vy = v*dp[0]/d
        vz = v*dp[1]/d

        pitch = -(-vy*kd+kp*(dp[0] - p*dp[0]/d))/g
        pitch_dot = np.zeros((1, pitch.shape[1]))

        X_2D = np.concatenate((py, pz, pitch, vy, vz, pitch_dot), axis=0)

        return X_2D

    @staticmethod
    def dynamic_3d(p0, pf, kd, kp):
        """

        :param p0: initial pose
        :param pf: final pose
        :param kd: control gain
        :param kp: control gain
        :return: 3D pose
        """

        # delta of the displacement and its norm
        dp = pf - p0
        d = np.linalg.norm(dp)
        d_xy = np.linalg.norm(dp[:2])
        dp = dp.reshape(dp.shape[0])
        state = PD(kd, kp, 0.0, 0.0, d)

        p = state[:, 0]
        v = state[:, 1]

        p = p.reshape(1, p.shape[0])
        v = v.reshape(1, v.shape[0])

        if d != 0.0:
            Cp = d_xy/d
            Sp = dp[2]/d
            if d_xy != 0.0:
                Cf = dp[0]/d_xy
                Sf = dp[1]/d_xy
            else:
                Cf = .0
                Sf = .0

        # position
        px = p0[0] + p*Cp*Cf
        py = p0[1] + p*Cp*Sf
        pz = p0[2] + p*Sp

        # velocities
        vx = v*Cp*Cf
        vy = v*Cp*Sf
        vz = v*Sp

        pitch = -(-vy*kd+kp*(dp[1] - p*dp[1]/d))/g
        pitch_dot = np.zeros((1, pitch.shape[1]))

        roll = -(-vx*kd + kp*(dp[0] + p*dp[0]/d))/g
        roll_dot = np.zeros((1, roll.shape[1]))

        yaw = np.zeros((1, roll.shape[1]))
        yaw_dot = np.zeros((1, roll.shape[1]))

        X_3D = np.concatenate((px, py, pz, pitch, roll, yaw, vx, vy, vz, pitch_dot, roll_dot, yaw_dot), axis=0)

        return X_3D


class Maneuver:

    @staticmethod
    def hover(ph, t, dt):
        """

        :param ph: hover pose
        :param t: time hovering
        :param dt: time differential
        :return: ph -- hover pose
        """

        N = int(t/dt)

        ph = ph.reshape(ph.shape[0], 1)
        ph[int(ph.shape[0]/2):] = 0.0
        hover = ph*np.ones((ph.shape[0], N))
        ph = np.concatenate((ph, hover), axis=1)

        return ph


def PD(kd, kp, p0, p0d, q_des):
    """

    :param kd: derivative gain
    :param kp: proportional gain
    :param p0: pose
    :param p0d: desired pose
    :param q_des: desired q
    :return: P:
    """

    # The differential equation
    def diff2(t, y):
        dy1 = y[1]
        dy2 = -kd * y[1] + kp * (q_des - y[0])
        return [dy1, dy2]

    t2 = np.linspace(0, 15, 1500)
    p0 = [p0, p0d]

    P = integrate.odeint(diff2, p0, t2, tfirst=True)

    ind = np.where(P[:, 0] >= q_des - 0.01)[0][0]
    P = P[:ind, :]
    return P
