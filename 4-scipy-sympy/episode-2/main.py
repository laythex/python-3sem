import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

data = np.loadtxt('system.txt', skiprows=1)
N = data.shape[1]
A, B = np.array_split(data, [N], axis=0)
B = np.transpose(B)

plt.bar(np.arange(N), np.transpose(sp.linalg.solve(A, B))[0])
plt.grid()
plt.gca().set_axisbelow(True)

plt.savefig('solution.png')

plt.show()
