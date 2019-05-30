
"""
Plannar Quadrotor control

authors: Jean-Bernard Uwineza & Zhao Hangquan
"""

import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from utils import util

controller = util.Controller()


def partA():

    def D2_init():
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        time_text.set_text('')
        pos_text.set_text('')
        pitch_text.set_text('')

        return ln, pos_text,time_text,pitch_text

    def D2_update(i):
        xdata.append(X_2d[0, i])
        ydata.append(X_2d[1, i])
        ln.set_data(xdata, ydata)
        print('Position:({0:.3f},{1:0.3f})'.format(X_2d[0, i], X_2d[1, i]))
        print('Pitch:{0:.3f}'.format(X_2d[2, i]))

        time_text.set_text(time_template % (0.01 * i))
        pos_text.set_text(pos_template % (X_2d[0, i], X_2d[1, i]))
        pitch_text.set_text(pitch_template % X_2d[2, i])

        return ln,  pos_text, time_text, pitch_text
    ##
    fig, ax = plt.subplots()
    xdata, ydata, zdata = [], [], []
    ln, = ax.plot([], [], 'ro', animated=False)
    time_template = 'Time elapased = %.1fs'
    pos_template = 'Current position = (%.2f,%.2f)'
    pitch_template = 'Pitch = %.2f'
    time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)
    pos_text = ax.text(0.05, 0.8, '', transform=ax.transAxes)
    pitch_text = ax.text(0.05, 0.7, '', transform=ax.transAxes)

    X_2d = []
    frames = []

    """ For Part A"""
    # 2D initial positions

    arr = input("Enter initial position coordinates, q0, separated by a blank space. (Example : 0 0) ")
    q0_2d = [[int(n)] for n in arr.split()]

    arr = input("Enter final vertical position coordinates, qh,  separated by a blank space. (Example : 4 5) ")
    qh_2d = [[int(n)] for n in arr.split()]
    qh_2d = np.array(qh_2d)

    zt_2d = eval(input('Enter the initial height (in meters). (Example: 2) '))

    T_2d = eval(input('Enter the time spent hovering (in seconds). (Example: 2) '))
    X_2d, dt = controller.control_2d(q0_2d, qh_2d, zt_2d, T_2d)

    t_2d = np.linspace(0, dt * X_2d.shape[1], X_2d.shape[1])  # shape[1] return back column

    Y_2d = X_2d[0, :]
    Z_2d = X_2d[1, :]
    n = Y_2d.shape
    n = n[0]
    n = n-1

    ani = FuncAnimation(fig, D2_update, frames=n, interval=5, repeat=False,
                        init_func=D2_init, blit=True)
    plt.xlabel('Y-position')
    plt.ylabel('Z-position')
    plt.title('The path of the Quadrotor in 2D')
    plt.show()

    labels_2d = ['Y-position', 'Z-position', 'Pitch', 'Y-velovity', 'Z-velocity', 'Pitch-dot']

    fig1 = plt.figure(1)
    for i in range(len(X_2d)):
        plt.subplot('23' + str(i + 1))
        plt.plot(t_2d, X_2d[i, :])
        plt.xlabel('Time')
        plt.ylabel(labels_2d[i])
        # plt.title(labels_2d[i] + ' state evolution')

    print("Plotting states' evolution...")
    plt.show(fig1)


def partB():
    """ For part B"""

    fig3 = plt.figure(3)
    ax_3d = Axes3D(fig3)
    X_3d = []
    ln_3d = ax_3d.scatter([], [], [], 'ro', animated=False)

    time_template = 'Time elapsed = %.1fs'
    pos_template = 'Current position = (%.2f,%.2f，%.2f)'
    angle_template = 'Pitch = (%.2f,%.2f，%.2f)'
    time_text = ax_3d.text2D(0.05, 0.9, '', transform=ax_3d.transAxes)
    pos_text = ax_3d.text2D(0.05, 0.8, '', transform=ax_3d.transAxes)
    angle_text = ax_3d.text2D(0.05, 0.7, '', transform=ax_3d.transAxes)

    arr = input("Enter initial position coordinates, q0, separated by a blank space. (Example : 0 0 0) ")
    q0_3d = [[int(n)] for n in arr.split()]
    q0_3d = np.array(q0_3d)

    arr = input("Enter final vertical position coordinates, qh,  separated by a blank space. (Example : 3 4 5) ")      # enter into the final position like 3 4 5
    qh_3d = [[int(n)] for n in arr.split()]
    qh_3d = np.array(qh_3d)

    zt_3d = eval(input('Enter the initial height (in meters). (Example: 2) '))   # enter into the height like 2

    T_3d = eval(input('Enter the time spent hovering (in seconds). (Example: 2) '))     # enter into the time like 3

    X_3d, dt = controller.control_3d(q0_3d, qh_3d, zt_3d, T_3d)
    t_3d = np.linspace(0, dt*X_3d.shape[1], X_3d.shape[1])

    a = X_3d[0, :]
    a = a.shape
    n = a[0]
    ax_3d.set_xlim3d(0,10)
    ax_3d.set_ylim3d(0, 10)
    ax_3d.set_zlim3d(0, 10)
    plt.ion()
    plt.title('The path of the Quadrotor in 3D')
    ax_3d.set_xlabel('X-axis')
    ax_3d.set_ylabel('Y-axis')
    ax_3d.set_zlabel('Z-axis')
    for i in range(0, n):
        ax_3d.scatter(X_3d[0, i*5], X_3d[1, i*5], X_3d[2, i*5], c='r',marker=".")
        print('the position:({0:.3f},{1:0.3f},{2:.3f})'.format(X_3d[0, i*5], X_3d[1, i*5],X_3d[2, i*5]))
        print('the angle(Pitch, Roll, Yaw):({0:.3f},{1:0.3f},{2:.3f})'.format(X_3d[3, i*5], X_3d[4, i*5],X_3d[5, i*5]))
        time_text.set_text(time_template % (0.05 * i))
        pos_text.set_text(pos_template % (X_3d[0, i*5],X_3d[1, i*5],X_3d[2, i*5]))
        angle_text.set_text(angle_template % (X_3d[3, i * 5], X_3d[4, i * 5], X_3d[5, i * 5]))

        plt.pause(0.01)
        if 5*i > (n-5):
            break

    labels_3d = ['X-position', 'Y-position', 'Z-position', 'Pitch', 'Roll', 'Yaw',
                 'X-velocity', 'Y-velovity', 'Z-velocity', 'Pitch-dot', 'Yaw-dot', 'Roll-dot']

    fig4 = plt.figure(4)
    for i in range(len(X_3d)):
        plt.subplot(4, 3, i + 1)
        plt.plot(t_3d, X_3d[i, :])
        plt.xlabel('Time')
        plt.ylabel(labels_3d[i])

    print("Plotting states' evolution...")
    plt.show(fig4)


def main():
    choice = eval(input("Please chose bewtween 2-D and 3-D. \n  2-D: 1 \n 3-D : 2 \n Your choice:  "))
    if choice == 1:
        partA()

    if choice == 2:
        partB()


if __name__ == "__main__":
    main()
