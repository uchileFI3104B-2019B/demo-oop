#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np


t = np.linspace(0.00001, 2 * np.pi, 1000)
x = np.sin(np.sqrt(10) * t**2) / t

fig = plt.figure(2)
fig.clf()

ax = fig.add_subplot(111)
ax.plot(t, x)

ax.set_xlim(0, 6.5)
ax.set_ylim(-1.55, 1.55)

ax_chico = fig.add_axes([0.6, 0.2, 0.25, 0.2])
ax_chico.plot(t[500:600], x[500:600])

fig.show()
