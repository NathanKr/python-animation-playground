import random
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight') # nice styling

x = []
y = []
index = count()

def animate(frame_index): 
    x.append(next(index))
    y.append(random.randint(0,5))
    plt.cla()
    plt.plot(x,y)


ani = FuncAnimation(plt.gcf(),animate,interval=1000)
plt.show()