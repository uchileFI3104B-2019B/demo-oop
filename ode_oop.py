#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import ode

'''
Vamos a resolver numericamente la ecuacion d2x/dx2 = dx/dt / t - 4 k t*22 x.
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

ax1 = fig.add_subplot(211)

t = np.linspace(0.0, 2 * np.pi, 1000)
x = analitica(t)

ax1.plot(t, x, 'b', label='analitica')

ax1.set_xlim(0, 6.5)
ax1.set_ylim(-1.1, 1.1)

ax1.set_xlabel('t')
ax1.set_ylabel('x')


# ---------------------------------
# Ahora integramos numericamente
# ---------------------------------

def f_to_solve(t, y, k=K):
    x, v = y
    return [v, v / t - 4 * k * t**2 * x]

# Condiciones iniciales
t0 = 1e-3
y0 = [np.sin(np.sqrt(10) * t0**2),
      2 * np.sqrt(K) * np.cos(np.sqrt(K) * t0**2) * t0]

# creamos el 'resolvedor'
r = ode(f_to_solve)
# r.set_integrator('dopri5', max_step=0.1, first_step=0.01)
r.set_integrator('dopri5')
r.set_initial_value(y0, t0)

# guardamos las variables a medida que progresamos
t_values = np.linspace(t0, 2 * np.pi, 1000)
x_values = np.zeros(len(t))
v_values = np.zeros(len(t))

for i in range(len(t_values)):
    r.integrate(t_values[i])
    x_values[i], v_values[i] = r.y


ax1.plot(t_values, x_values, 'g', label='RK4')

ax2 = fig.add_subplot(212)
ax2.plot(t_values, np.fabs(analitica(t_values) - x_values), 'r')
# ax2.plot(t_values, np.log10(np.fabs(analitica(t_values) - x_values)), 'r')
ax2.set_xlabel('t')
ax2.set_ylabel('analitica - rk4')

ax1.legend()
plt.show()
plt.draw()
