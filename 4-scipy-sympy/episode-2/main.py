import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

with open('system.txt') as file:
    N = int(file.readline())
    A, B = np.array_split(np.loadtxt(file.readlines()), [N], axis=0)
    B = np.transpose(B)

plt.bar(np.arange(N), np.transpose(sp.linalg.solve(A, B))[0])
plt.grid()
plt.gca().set_axisbelow(True)

plt.savefig('solution.png')

plt.show()
