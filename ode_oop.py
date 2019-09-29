#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import RK45


'''
Vamos a resolver numericamente la ecuacion d2x/dx2 = dx/dt / t - 4 k t**2 x.
La solucion analitica es x(t) = sin(sqrt(k) * t**2)
'''

K = 10.
def analitica(t, k=K):
    return np.sin(np.sqrt(K) * t**2)

# ---------------------------------
# Veamos la solución analitica
# ---------------------------------

fig = plt.figure(1)
fig.clf()

# ax1 = fig.add_subplot(111)
ax1 = fig.add_subplot(211)

t = np.linspace(0.0, 2 * np.pi, 1000)
x = analitica(t)

ax1.plot(t, x, 'b', label='analitica')

ax1.set_xlim(0, 6.5)
ax1.set_ylim(-1.1, 1.1)

ax1.set_xlabel('t')
ax1.set_ylabel('x')

# ------------------
# Solucion numerica
# ------------------

def fun_a_integrar(t, y, k=K):
    y, v = y
    return [v, v/t - 4 * k * t**2 * y]

def fun_para_RK45(t, y):
    return fun_a_integrar(t, y, k=K)


t0 = 1e-3
y0 = [np.sin(np.sqrt(K) * t0**2),
      2 * np.sqrt(K) * np.cos(np.sqrt(K) * t0**2) * t0]

resolvedor = RK45(fun_para_RK45, t0, y0, 7.)

t_sol = [resolvedor.t]
y_sol = [resolvedor.y]
while resolvedor.t < 7.:
    resolvedor.step()
    t_sol.append(resolvedor.t)
    y_sol.append(resolvedor.y)

t_sol = np.array(t_sol)
y_sol = np.array(y_sol)


ax1.plot(t_sol, y_sol[:,0], 'rx', label="RK45")

ax2 = fig.add_subplot(212)
ax2.plot(t_sol, np.log10(np.fabs(analitica(t_sol) - y_sol[:,0])), 'r.')
ax2.set_xlabel('t')
ax2.set_ylabel('analitica - rk45')

ax1.legend()
plt.show()

"""
Les recomiendo explorar como se achico o agrando el paso de la integracion.
ej:
dt = t_sol[1:] - t_sol[:-1]  # dt se achica o se agranda conforme avanza la
                             # integracion?
"""
