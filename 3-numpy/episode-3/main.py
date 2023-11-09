import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

data = np.loadtxt('start.dat')
E = np.diag(np.ones(data.size))
A = E + np.roll(-E, 1, 0)

fig, ax = plt.subplots()
ln, = ax.plot(data)
ax.grid(True)


def update(frame):
    global data
    data = np.matmul(E - A / 2, data)
    ln.set_ydata(data)
    ax.set_title(f'Frame {frame}')
    return ln,


anim = FuncAnimation(fig, update, 255)

anim.save('process.gif')
plt.show()
