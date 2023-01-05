"""
This file contains Python equations from the on-c-e model 
 m0202_loads.txt

For interactive analysis open the file
in an interactive shell including
Spyder, Jupyter Notebook or Komodo IDE 
""" 
from __future__ import division
from __future__ import print_function
import os
import sys
from sympy import *
from numpy import *
import numpy.linalg as LA
from collections import OrderedDict
from unum import Unum
from once.calunit import *
sys.path.append('D:\\Egnyte\\Shared\\01_General\\03_Engineering\\05_Tracker\\14_EngDocs\\projects\\0253_ast_softbank_india\\ast_calcs_softbank')

# begin equations
#
# section: Rotation Models and Tests
pi = 3.141  #- constant
J1 = (0.344*IN**4).asUnit(CM**4)  #- polar moment of inertia
G1 = (11500. * KSI).asUnit(MPA)  #- steel shear modulus
cg = (20. * IN).asUnit(CM)  #- mass distance from pivot pin
gratio = .0909  #- gear ratio
modwt_3 = (3 * 400 * LBF).asUnit(N)  #- weight of modules for 3 tables
L_3 = (360. * IN).asUnit(CM)  #- location of SDOF mass for 3 tables
rotmass_3 = gratio*modwt_3 / G  #- reduce rotation mass - 3 tables
I_3 = rotmass_3*cg**2  #- mass moment of inertia
Kt_3 = (J1 * G1 / L_3)  #- rotational stiffness
freq_3 = (1/(2*pi) * (Kt_3 / I_3)**.5)  #- rotational frequency - 3 tables
L_10 = (2400. * IN).asUnit(M)  #- location of SDOF mass at end of row
modwt_1 = (400 * LBF).asUnit(N)  #- weight of modules for 1 table
rotmass_1 = gratio*modwt_3 / G  #- reduce rotation mass - edge table
I_1 = rotmass_1*cg**2  #- mass moment of inertia - 1 table
Kt_10 = (J1 * G1 / L_10)  #- rotational stiffness - edge table
freq_10 = (1/(2*pi) * (Kt_10 / I_1)**.5)  #- rotational frequency - edge table
radius_b = 1.15*IN  #- outside radius of pinion
theta1 = 10/57  #- 1 degree table rotation
COFss = 0.9  #- friction coefficient for ss to ss
COF27 = 0.2  #- friction coefficient for ss to ZA 27
torque_3 = Kt_3 * theta1  #- rotation torque - 3 tables
R3 = torque_3/cg/gratio  #- Pinion reaction - 3 tables
se_3 = torque_3**2 * L_3 / (2 * J1 * G1)  #- strain energy - 3 tables
frictorq3a = COFss * R3 * radius_b  #- friction torque - ss
de3a = frictorq3a * theta1  #- damping energy - ss
equivdamp3a = de3a / (pi * se_3)  #- damping ratio - ss
frictorq3b = COF27 * R3 * radius_b  #- friction torque - ZA 27
de3a = frictorq3b * theta1  #- damping energy - ZA 27
equivdamp3b = de3a / (pi * se_3)  #- damping ratio - ZA 27
#
# section: Rotation Design Values and Displacement Check
#
# section: Static and Dynamic Gust Coefficients
Vd_b = 39*M/S  #- basic design 3 sec gust at 10 m
Vo_b = 22*M/S  #- basic operation 3 sec gust at 10 m
k_1 = 0.92  #- low hazard risk coefficient
k_2 = 1.00  #- terrain Cat 2, structure Class A
k_3 = 1.0  #- topography
k_h = 0.8  #- height factor structure < 10 m
k_d = 0.9  #- direction factor
K_p = 0.6 * PA*(S**2/M**2)  #- wind pressure constant
Vo_z = Vo_b**2 * K_p * k_1 * k_2 * k_3 * k_h  #- operation wind design pressure
Vd_z = Vd_b**2 * K_p * k_1 * k_2 * k_3 * k_h  #- mapped wind design pressure
#
# section: Model Design Wind Pressures
#
# section: Seismic Model and Loads
W_1 = (500 *LBF).asUnit(N)  #- seismic weight of table
Z_1 = 0.1  #- low seismicity zone
R_1 = 4.0  #- braced frame
DF_1 = 1.4  #- damping factor
Sa_g = 2.5  #- spectral acceleration coefficient
I_1 = 1.0  #- importance factor
A1_b = (Z_1 * I_1 * Sa_g)/(2 * R_1)  #- spectrum value
A2_b = Z_1 / 2.  #- minimum spectrum value
A_b = max(A1_b,A2_b)  #- design spectrum value
V1_B = A_b * W_1 / 2  #- base shear per A-frame
