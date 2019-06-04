def draw_figure(X_3d, dt):
    fig3 = plt.figure(2)
    ax_3d = Axes3D(fig3)
    ax_3d.set_xlim3d(0,20)
    ax_3d.set_ylim3d(0, 20)
    ax_3d.set_zlim3d(0, 20)
    plt.ion()
    plt.title('The path of the Quadrotor in 3D')
    ax_3d.set_xlabel('X-axis')
    ax_3d.set_ylabel('Y-axis')
    ax_3d.set_zlabel('Z-axis')
    time_text = ax_3d.text2D(0.05, 0.9, '', transform=ax_3d.transAxes)
    pos_text = ax_3d.text2D(0.05, 0.8, '', transform=ax_3d.transAxes)
    angle_text = ax_3d.text2D(0.05, 0.7, '', transform=ax_3d.transAxes)


    t_3d = np.linspace(0, dt * X_3d.shape[1], X_3d.shape[1])

    a = X_3d[0, :]
    a = a.shape
    n = a[0]

    for i in range(0, n):
        ax_3d.scatter(X_3d[0, i * 5], X_3d[1, i * 5], X_3d[2, i * 5], c='r', marker=".")
        print('the position:({0:.3f},{1:0.3f},{2:.3f})'.format(X_3d[0, i * 5], X_3d[1, i * 5], X_3d[2, i * 5]))
        print('the angle(Pitch, Roll, Yaw):({0:.3f},{1:0.3f},{2:.3f})'.format(X_3d[3, i * 5], X_3d[4, i * 5],
                                                                              X_3d[5, i * 5]))
        time_text.set_text(time_template % (0.05 * i))
        pos_text.set_text(pos_template % (X_3d[0, i * 5], X_3d[1, i * 5], X_3d[2, i * 5]))
        angle_text.set_text(angle_template % (X_3d[3, i * 5], X_3d[4, i * 5], X_3d[5, i * 5]))

        plt.pause(0.01)
        if 5 * i > (n - 5):
            break

    labels_3d = ['X-position', 'Y-position', 'Z-position', 'Pitch', 'Roll', 'Yaw',
                 'X-velocity', 'Y-velovity', 'Z-velocity', 'Pitch-dot', 'Yaw-dot', 'Roll-dot']

    fig4 = plt.figure(3)
    for i in range(len(X_3d)):
        plt.subplot(4, 3, i + 1)
        plt.plot(t_3d, X_3d[i, :])
        plt.xlabel('Time')
        plt.ylabel(labels_3d[i])

    print("Plotting states' evolution...")
    plt.show(fig4)

def navigation(waypoints):
    """ For part B"""






    arr = input("Enter initial position coordinates, q0, separated by a blank space. (Example : 0 0 0) ")
    q0_3d = [[int(n)] for n in arr.split()] #convert it into list
    q0_3d = np.array(q0_3d)

    arr = input("Enter final vertical position coordinates, qh,  separated by a blank space. (Example : 3 4 5) ")      # enter into the final position like 3 4 5
    qh_3d = [[int(n)] for n in arr.split()]
    qh_3d = np.array(qh_3d)

    zt_3d = eval(input('Enter the initial height (in meters). (Example: 2) '))   # enter into the height like 2

    T_3d = eval(input('Enter the time spent hovering (in seconds). (Example: 2) '))     # enter into the time like 3

    X_3d, dt = controller.control_3d(q0_3d, qh_3d, zt_3d, T_3d)
    draw_figure(X_3d, dt)

