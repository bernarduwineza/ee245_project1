import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
quadrotor_length=0.046
fig = plt.figure()
ax_3d = Axes3D(fig)

major_ticks = np.arange(0, 20, 5)
minor_ticks = np.arange(0, 20, 0.1)

ax_3d.set_xlim3d(0, 20)
ax_3d.set_ylim3d(0, 20)
ax_3d.set_zlim3d(0, 20)
# ax_3d.set_xticks()
# ax_3d.set_xticks(major_ticks)
# ax_3d.set_xticks(minor_ticks, minor=True)
# ax_3d.set_yticks(major_ticks)
# ax_3d.set_yticks(minor_ticks, minor=True)
# ax_3d.set_zticks(major_ticks)
# ax_3d.set_zticks(minor_ticks, minor=True)
# ax_3d.grid(which='both')
# ax_3d.grid(which='minor', alpha=0.2)
# ax_3d.grid(which='major', alpha=0.5)


obs1=ax_3d.bar3d(2, 2, 0, 10, 10, 10)
#obs2=ax_3d.bar3d(8, 0, 2, 4, 1, 1)
quadrotor=ax_3d.bar3d(0, 0, 0, 0.023, 0.023, 0)
C_obs=ax_3d.bar3d(2-quadrotor_length/2, 2-quadrotor_length/2, 0, 10+quadrotor_length, 10+quadrotor_length, 10)

# init
original_point=(0, 0)
destination_point=(20, 20)
gird_length=0.01
# plan
open=[(0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
goal_set=open[4]
close=[]
node=len(open)
past_cost=[]
sucess='sucess'

past_cost.append(0)
for i in range(node-1):
    past_cost.append(math.inf)

while:
    current=open[0]
    open.remove(open[0])
    close.append(current)
    if current == goal_set:
        return sucess and path






plt.show()


