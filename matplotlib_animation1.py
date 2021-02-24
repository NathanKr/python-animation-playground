import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight') # nice styling

x = []
y = []

def animate(frame_index): 
    x.append(next(frame_index))
    y.append(random.randint(0,5))
    plt.cla()
    plt.plot(x,y)


ani = FuncAnimation(plt.gcf(),animate,interval=1000)
plt.show()