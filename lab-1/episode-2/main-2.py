import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

with open('2.dat') as file:
    data = [list(map(float, entry.split())) for entry in file.readlines()]
    n, x, y = int(len(data) / 2), data[::2], data[1::2]

fig, ax = plt.subplots()
ln, = ax.plot([], [])
ax.set_xlim(0, 16)
ax.set_ylim(-10, 12)
ax.set_yticks(np.linspace(-10, 12, 12))
ax.grid(True)


def update(frame):
    ln.set_data(x[frame], y[frame])
    ax.set_title(f'Frame {frame}')
    return ln,


anim = FuncAnimation(fig, update, frames=n)

anim.save('episode-2.gif')
plt.show()
