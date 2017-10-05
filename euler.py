#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Implementacion del método de Euler simple para demostrar debugging.
'''

import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import ode

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

ax1 = fig.add_subplot(211)

t = np.linspace(0.0, np.pi, 1000)
x = analitica(t)

ax1.plot(t, x, 'b', label='analitica')

ax1.set_xlim(0, 3.5)
ax1.set_ylim(-1.1, 1.1)

ax1.set_xlabel('t')
ax1.set_ylabel('x')


# ---------------------------------
# Ahora usamos el método de Euler
# ---------------------------------

def f_a_integrar(t, y, k=K):
    #import pdb; pdb.set_trace()  # XXX BREAKPOINT
    # Intentar comandos l, s, n dentro del debugger
    x, v = y
    return [v, v / t - 4 * k * t**2 * x]

def euler_step(t, y, dt):
    x, v = y
    f0, f1 = f_a_integrar(t, y)
    x_new = x + dt * f0
    v_new = v + dt * f1
    return [x_new, v_new]

# # Condiciones iniciales
# t0 = 0
# y0 = [0, 0]
#
# n_steps = np.int(1e5)
# dt = (np.pi - t0) / n_steps
#
# t_values = np.linspace(t0, np.pi, n_steps)
# x_values = np.zeros(n_steps)
# v_values = np.zeros(n_steps)
#
# x_values[0] = y0[0]
# v_values[0] = y0[1]
#
# for i in range(1, n_steps):
#     x_new, v_new = euler_step(t_values[i-1], [x_values[i-1], v_values[i-1]], dt)
#     x_values[i] = x_new
#     v_values[i] = v_new


# Solucion al problema anterior
t0 = 1e-3
y0 = [np.sin(np.sqrt(10) * t0**2),
      2 * np.sqrt(K) * np.cos(np.sqrt(K) * t0**2) * t0]

n_steps = np.int(1e5)
dt = (np.pi - t0) / n_steps
t_values = np.linspace(t0, np.pi, n_steps)
x_values = np.zeros(n_steps)
v_values = np.zeros(n_steps)

x_values[0] = y0[0]
v_values[0] = y0[1]

for i in range(1, n_steps):
    x_new, v_new = euler_step(t_values[i-1], [x_values[i-1], v_values[i-1]], dt)
    x_values[i] = x_new
    v_values[i] = v_new

ax1.plot(t_values, x_values, 'g', label='Euler')
ax1.legend()


# Plotear las diferencias
ax2 = fig.add_subplot(212)
ax2.plot(t_values, analitica(t_values) - x_values, 'r')
ax2.set_xlabel('t')
ax2.set_ylabel('analitica - euler')


plt.show()
plt.draw()
