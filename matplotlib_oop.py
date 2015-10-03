#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure(1)
fig.clf()
t = np.linspace(0.00001, 2 * np.pi, 1000)
x = np.sin(np.sqrt(10) * t**2) / t

ax = plt.subplot(111)

ax.plot(t, x)

ax.set_xlim(0, 6.5)
ax.set_ylim(-1.55, 1.55)

ax.set_xlabel('t')
ax.set_ylabel('x')

# # Hagamos un subplot
# # estas funciones no estan implementadas en formato 'procedural'
#
# ax2 = fig.add_axes([0.6, 0.15, 0.25, 0.2])
# ax2.plot(t, 1/t)
#
# ax2.set_xlim(0, 6)
# ax2.set_ylim(0, 3)

plt.show()
plt.draw()
