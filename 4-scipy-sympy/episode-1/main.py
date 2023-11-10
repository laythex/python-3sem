import sympy as syp
from sympy.abc import lamda, mu, rho

A = syp.zeros(9, 9)
A[3, 0] = -(lamda + 2 * mu)
A[4, 1] = A[5, 2] = -mu
A[6, 0] = A[8, 0] = -lamda
A[0, 3] = A[1, 4] = A[2, 5] = -1 / rho

print(A.eigenvals())
