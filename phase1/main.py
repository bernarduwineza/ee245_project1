"""
Plannar Quadrotor ocntrol

authors: Jean-Bernard Uwineza & Zhao Hangquan
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from util import *

# TODO: Use user inputs to select either 2D or 3D case.
# TODO: Ask user to input initial and final poses for the quad
# TODO: Use pen to draw the trajectory of the drone

controller = Controller()
""" For Part A"""

# 2D initial positions
q0_2d = np.array([[.0], [.0]])
qh_2d = np.array([[5.0], [5.0]])

zt_2d = 2.0         # hover attitude
T_2d = 2.0          # time hovering

X_2d, dt = controller.control_2d(q0_2d, qh_2d, zt_2d, T_2d)
t_2d = np.linspace(0, dt*X_2d.shape[1], X_2d.shape[1])

fig1 = plt.figure(1)
plt.plot(X_2d[0,:], X_2d[1,:])
plt.xlabel('Y-position')
plt.ylabel('Z-position')
plt.title('The path of the Quadrotor in 2D')
# plt.show()

labels_2d = ['Y-position', 'Z-position', 'Pitch', 'Y-velovity', 'Z-velocity', 'Pitch-dot']
fig2 = plt.figure(2)
for i in range(len(X_2d)):
    plt.subplot('23' + str(i+1))
    plt.plot(t_2d, X_2d[i, :])
    plt.xlabel('Time')
    plt.ylabel(labels_2d[i])
    # plt.title(labels_2d[i] + ' state evolution')


""" For part B"""
q0_3d = np.array([[0.0], [0.0], [0.0]])
qh_3d = np.array([[5.0], [5.0], [5.0]])

zt_3d = 2.0
T_3d = 2.0

X_3d, dt = controller.control_3d(q0_3d, qh_3d, zt_3d, T_3d)
t_3d = np.linspace(0, dt*X_3d.shape[1], X_3d.shape[1])

fig3 = plt.figure(3)
ax = Axes3D(fig3)
ax.scatter(X_3d[0, :], X_3d[1, :], X_3d[2, :])
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

plt.title('The path of the Quadrotor in 3D')

labels_3d = ['X-position', 'Y-position', 'Z-position', 'Pitch', 'Roll', 'Yaw',
             'X-velocity', 'Y-velovity', 'Z-velocity', 'Pitch-dot', 'Yaw-dot', 'Roll-dot']

fig4 = plt.figure(4)
for i in range(len(X_3d)):
    plt.subplot(4, 3, i+1)
    plt.plot(t_3d, X_3d[i, :])
    plt.xlabel('Time')
    plt.ylabel(labels_3d[i])
plt.show()
