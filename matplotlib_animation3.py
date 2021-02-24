import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

limit = 2
fig = plt.figure()
ax = plt.axes(xlim=(-limit, limit), ylim=(0, limit))
line, = ax.plot([], [], lw=2)

x = np.linspace(-limit, limit, 1000)
dx = 0.1
points = 1 + 2 * limit / dx 


def animate(frame_index): 
    x_p = -2 + (frame_index % points) * dx
    if x_p > limit:
        x_p = -limit
        
    y_p = y(x_p)
    plt.cla()
    plt.grid()
    plt.plot(x,y(x))
    plt.plot(x_p,y_p,'o',markersize=10)


def y(_x):
    return _x ** 2

ani = FuncAnimation(fig,animate)
plt.show()
