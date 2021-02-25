import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

limit = 2
fig = plt.figure()
ax = plt.axes(xlim=(-limit, limit), ylim=(0, 2*limit))
line1, = ax.plot([], [], lw=2)
line2, = ax.plot([], [],'o',markersize=10)


x = np.linspace(-limit, limit, 1000)
dx = 0.1
points = 1 + 2 * limit / dx 


def animate(frame_index): 
    x_p = -2 + (frame_index % points) * dx
    if x_p > limit:
        x_p = -limit
        
    line1.set_data(x,y(x))
    line2.set_data(x_p,y(x_p))


def y(_x):
    return _x ** 2

ani = FuncAnimation(fig,animate)
plt.grid()
plt.show()
