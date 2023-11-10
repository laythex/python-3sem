import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import sympy as syp
from sympy.abc import x


def diff_equation(_, f): return -2 * f


y = syp.Function('y')
eq = syp.Eq(syp.Derivative(y(x), x), -2 * y(x))
sol_sympy = syp.lambdify(x, syp.dsolve(eq, ics={y(0): syp.sqrt(2)}).rhs, 'numpy')

sol_scipy = sp.integrate.solve_ivp(diff_equation, [0, 10], [np.sqrt(2)])

fig, ax = plt.subplots(2, 1, figsize=(10, 8))

xrange = np.linspace(0, 10, 100)
ax[0].plot(xrange, sol_sympy(xrange), label='SymPy')
ax[0].plot(sol_scipy.t, sol_scipy.y[0], label='SciPy')
ax[1].plot(sol_scipy.t, sol_scipy.y[0] - sol_sympy(sol_scipy.t))
ax[0].legend()
ax[0].grid()
ax[1].grid()
ax[0].set_title('Solutions')
ax[1].set_title('Difference')

plt.savefig('ode-solutions.png')
plt.show()
