import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



"""
Plannar Quadrotor ocntrol

authors: Jean-Bernard Uwineza & Zhao Hangquan
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from util import *
from model.quadrotor import Quadrotor

from utils import controller
from utils.quadPlot import plot_quad_3d
# TODO: Use user inputs to select either 2D or 3D case.
# TODO: Ask user to input initial and final poses for the quad
# TODO: Use pen to draw the trajectory of the drone

controller = Controller()
### this is for two dimension
fig, ax = plt.subplots()
xdata, ydata, zdata= [], [], []

ln, = ax.plot([], [], 'ro', animated=False)

X_2d=[]
frames=[]
stop=0
###
def D2_init():


    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    return ln,

def D2_update(i):

    xdata.append(X_2d[0, i])
    ydata.append(X_2d[1, i])
    ln.set_data(xdata, ydata)

    return ln,

###this is for 3-dimension

fig3 = plt.figure(3)
ax_3d = Axes3D(fig3)
X_3d=[]
ln_3d=ax_3d.scatter([],[],[],'ro', animated=False)

####
def D3_init():


    ax_3d.set_xlim3d(0,10)
    ax_3d.set_ylim3d(0, 10)
    ax_3d.set_zlim3d(0, 10)

    return ln_3d,

def D3_update(i):

    xdata.append(X_3d[0, :])
    ydata.append(X_3d[1, :])
    zdata.append(X_3d[2, :])


    #ln_3d.set_data(xdata, ydata,zdata)
    ln_3d = ax_3d.scatter(xdata, ydata, zdata, 'ro', animated=False)


    return ln_3d,



def partA():
    global X_2d
    global frames
    """ For Part A"""
    ###my code:
    pos = (0, 0, 0)
    attitude = (0, 0, 0)
    drone = Quadrotor(pos, attitude)
    ###
    # 2D initial positions
    ##zhq:

    arr = input("q0_2d:")  ##输入一个一维数组，每个数之间使空格隔开
    q0_2d = [[int(n)] for n in arr.split()]  ##将输入每个数以空格键隔开做成数组##
    q0_2d = np.array(q0_2d)

    arr = input("qh_2d:")  ##输入一个一维数组，每个数之间使空格隔开
    qh_2d = [[int(n)] for n in arr.split()]  ##将输入每个数以空格键隔开做成数组##
    qh_2d = np.array(qh_2d)

    zt_2d = eval(input('Enter the initial height(in meters):'))

    T_2d = eval(input('Enter the time:'))
    ##
    # q0_2d = np.array([[.0], [.0]])      # y-position, z-posittion
    # qh_2d = np.array([[5.0], [5.0]])    # y-position, z-position
    #
    # zt_2d = q0_2d[1] + 2.0      # vertical height to reach
    # T_2d = 2.0                  # time hovering
    ###

    ##

    X_2d, dt = controller.control_2d(q0_2d, qh_2d, zt_2d,
                                     T_2d)  ## enter into the parameter## and return back all the possible data
    t_2d = np.linspace(0, dt * X_2d.shape[1], X_2d.shape[1])  ##shape[1] return back column

    # fig1 = plt.figure(1)
    # plt.plot(X_2d[0, :], X_2d[1, :])
    # plt.xlabel('Y-position')
    # plt.ylabel('Z-position')
    # plt.title('The path of the Quadrotor in 2D')
    # # plt.show()

    # labels_2d = ['Y-position', 'Z-position', 'Pitch', 'Y-velovity', 'Z-velocity', 'Pitch-dot']
    # fig2 = plt.figure(2)
    # for i in range(len(X_2d)):
    #     plt.subplot('23' + str(i + 1))
    #     plt.plot(t_2d, X_2d[i, :])
    #     plt.xlabel('Time')
    #     plt.ylabel(labels_2d[i])
    #     # plt.title(labels_2d[i] + ' state evolution')
    Y_2d=X_2d[0, :]
    Z_2d=X_2d[1, :]
    n=Y_2d.shape
    n=n[0]
    n=n-1
    frames=n

    ani = FuncAnimation(fig, D2_update, frames=n,interval=5,repeat=True,
                        init_func=D2_init, blit=True)
    plt.show()

def partB():
    """ For part B"""
    global X_3d

    arr = input("q0_3d:")
    q0_3d = [[int(n)] for n in arr.split()]
    q0_3d = np.array(q0_3d)

    arr = input("qh_3d:")
    qh_3d = [[int(n)] for n in arr.split()]
    qh_3d = np.array(qh_3d)

    zt_3d = eval(input('Enter the initial height(in meters):'))

    T_3d = eval(input('Enter the time:'))

    # q0_3d = np.array([[0.0], [0.0], [0.0]])
    # qh_3d = np.array([[5.0], [5.0], [5.0]])
    #
    # zt_3d = q0_3d[2] + 2.0
    # T_3d = 2.0
    #
    X_3d, dt = controller.control_3d(q0_3d, qh_3d, zt_3d, T_3d)
    t_3d = np.linspace(0, dt*X_3d.shape[1], X_3d.shape[1])

    # fig3 = plt.figure(3)
    # ax_3d = Axes3D(fig3)

    a=X_3d[0, :]
    a=a.shape
    n=a[0]
    ax_3d.set_xlim3d(0,10)
    ax_3d.set_ylim3d(0, 10)
    ax_3d.set_zlim3d(0, 10)
    plt.ion()
    for i in range(0,n):
        ax_3d.scatter(X_3d[0, i*5], X_3d[1, i*5], X_3d[2, i*5])
        plt.pause(0.01)
        if 5*i>n:
            break
    #ani = FuncAnimation(fig3, D3_update, frames=n,interval=5,
     #                   init_func=D3_init, blit=True)
    # ax.scatter(X_3d[0, :], X_3d[1, :], X_3d[2, :])
    # ax.set_xlabel('X-axis')
    # ax.set_ylabel('Y-axis')
    # ax.set_zlabel('Z-axis')
    #
    # plt.title('The path of the Quadrotor in 3D')
    #
    # labels_3d = ['X-position', 'Y-position', 'Z-position', 'Pitch', 'Roll', 'Yaw',
    #              'X-velocity', 'Y-velovity', 'Z-velocity', 'Pitch-dot', 'Yaw-dot', 'Roll-dot']
    #
    # fig4 = plt.figure(4)
    # for i in range(len(X_3d)):
    #     plt.subplot(4, 3, i + 1)
    #     plt.plot(t_3d, X_3d[i, :])
    #     plt.xlabel('Time')
    #     plt.ylabel(labels_3d[i])
    plt.show()



def main():
    choice=eval(input("choice: 2-dimension: 1 ;3-dimension : 2:"))
    if choice ==1:
         partA()

    if choice ==2:
        partB()






main()

