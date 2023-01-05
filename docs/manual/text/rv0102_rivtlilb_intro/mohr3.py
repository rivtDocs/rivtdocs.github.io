# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 05:01:53 2017

@author: rhhppc64
"""

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

circ = plt.Circle((0.5, 0), 0.3, facecolor='none', edgecolor='red')
ax.add_patch(circ)

ax.legend([circ], ['Stress State'])

# The rest is purely optional and just for appearance.
ax.axhline(0, color='black')
ax.axvline(0, color='black')
ax.margins(0.05)
ax.axis('scaled')
ax.set(xlabel=r'Normal Stress', ylabel=r'Shear Stress')

plt.show()