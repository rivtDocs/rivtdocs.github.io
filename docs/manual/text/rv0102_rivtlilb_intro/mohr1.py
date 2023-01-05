# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 04:30:56 2017

@author: rhhppc64
"""

from mpl_toolkits.mplot3d import *     # für Druckplots benötigt
from matplotlib import cm
from math import *                     # für pi und exp benötigt
from scipy.special import *            # für expn benötigt
import matplotlib.pyplot as plt        # für Plotting in 2D/3D benötigt
import numpy as np                     # für für Arrays benötigt
import matplotlib.lines as mlines
import os
clear = lambda: os.system('cls')
clear()
#==============================================================================
#                               Mohr Cirlce
#==============================================================================

#depth = 3000.0                  # Reservoirtiefe
#density = 2700.0                # Dichte des überlagernden Gesteins
#G = 12700.0                     # shear modulus [MPa]
#E = 26000.0                     # Young´s modulus in [MPa]
#sv = 9.81*density*depth/1e6     # vertical stress
#sh = 0.5*sv                     # minimum horizontal stress
cf1 = 4.0                        # Cohesion C Fault1 [MPa] 
muef1 = 0.5                      # coefficient of friction  [MPa]
#f1dip = 45                      # Einfallen der Störung
p0 = 15.0                        # initial pore pressure [MPa]

# Mohr failure criterion ##
sigman = np.zeros((80))
tauf1 = np.zeros((80))
for i in range(0,80):
    sigman[i] = i
    tauf1[i] = muef1*sigman[i]+cf1 # Bruchgerade

## Stresses ##
sH = 60.0
sh = 30.0   
smean = float((sH+sh)/2)         # Kreismittelpunkt
shear = float((sH-sh)/2)         # Kreisradius

## Effective Stresses ##
sHeff = sH-p0                       # effektive Vertikalspannung
sheff = sh-p0                       # effektive Horizontalspannung
smeaneff = float((sHeff+sheff)/2)   # Kreismittelpunkt
sheareff = float((sHeff-sheff)/2)   # Kreisradius

## Plotting ## 
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
plt.plot(sigman, tauf1, "b", linewidth=1, linestyle="-", label="Bruchgerade")
ax.axis('scaled')
mohr=plt.Circle((smean,0), radius=shear, color='g', fill=False, label = "Mohr")
mohreff=plt.Circle((smeaneff,0), radius=sheareff, color='r', fill=False)
plt.title("Mohrkreise bei ...")
ax.set_xlabel('$\sigma$ [MPa]', fontsize=12)
ax.set_ylabel('$\tau$ [MPa]', fontsize=12)
plt.xticks(np.arange(0, 90, 10))
plt.yticks(np.arange(0, 45, 5))
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0., numpoints = 1)
ax.add_patch(mohr)
ax.add_patch(mohreff)
plt.show()