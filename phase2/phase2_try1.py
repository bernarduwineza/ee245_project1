import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax_3d = Axes3D(fig)
ax_3d.set_xlim3d(0, 20)
ax_3d.set_ylim3d(0, 20)
ax_3d.set_zlim3d(0, 20)
obs1=ax_3d.bar3d(2, 2, 0, 10, 10, 10)
##obs2=ax_3d.bar3d(8, 0, 2, 4, 1, 1)

plt.show()


