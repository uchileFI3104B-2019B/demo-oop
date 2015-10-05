#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np


plt.figure(1)
t = np.linspace(0.00001, 2 * np.pi, 1000)
x = np.sin(np.sqrt(10) * t**2) / t

plt.plot(t, x)

plt.xlim(0, 6.5)
plt.ylim(-1.55, 1.55)


plt.xlabel('t')
plt.ylabel('x')

plt.show()
plt.draw()
