"""
This file contains Python equations from the on-c-e model 
 m0301_track.txt

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
# section: Track Design
#
# section: Exterior Track Properties
A_e =   (84 * IN**2).asUnit(CM**2)  #- cross section area - half
Wt_e =  (169 * LBF/FT).asUnit(N/M)  #- segment unit weight - full
Sxe_m = (80 * IN**3).asUnit(CM**3)  #- minimum section modulus - half
Lne_t = (6.7 * FT).asUnit(M)  #- segment length
f_c =   (3 * KSI).asUnit(N/M**2)  #- design compression strength
fp_c = 3000  #- compression strength - no units
gamma_c = (145 * LBF/FT**3).asUnit(N/M**3)  #- concrete density
phi_b = 0.9  #- bending strength reduction factor
phi_v = 0.85  #- shear strength reduction factor
Vn_1 = (phi_v * 2 * fp_c**.5 * PSI).asUnit(MPA)  #- Track shear stress capacity
Mor_1 = (phi_b * 5 * fp_c**.5 * PSI).asUnit(MPA)  #- Track MOR - ACI 318 22-2
Vn_3 = (Vn_1 * A_e * 0.5)  #- 1/2 Track allowable shear
Mn_2 = Sxe_m * Mor_1  #- 1/2 Track moment capacity
Pu_2 = A_e * Mor_1  #- 1/2 Track axial capacity
#
# section: Exterior Track D/C Ratios
Wte_s = (1100 * LBF).asUnit(N)  #- weight of track section - full
Ru_2 = (670 * LBF).asUnit(N)  #- uplift reaction from RISA analysis
DF_1 = 0.9  #- dead load factor -
DF_2 = 1.2  #- dead load factor +
V1_d = 2.4 * KN  #- shear demand
DC_1 = Ru_2 / (DF_1 *  Wte_s)  #- Ballast  D/C ratio - interior stow
Md_2 = DF_2 * 550 *LBF * 1.5*FT  #- Beam bending demand
DC_2 = Md_2 / Mn_2  #- Beam bending D/C ratio
DC_3 = V1_d / Vn_3  #- Shear D/C ratio
DC_T =  DC_2 + DC_3  #- Shear interaction ratio
Poe_u =  11.5*IN * 1.5*IN * Po_1  #- Pull out capacity
Po_1 = (phi_v * 4 * fp_c**.5 * PSI)  #- Track unit pull out capacity
DC_b = 0.67 * (Ru_2 / Poe_u)  #- Pull out D/C ratio
#
# section: Slew Drive Base D/C Ratios
To_1 = (530*FT*LBF).asUnit(N*M)  #- peak operational torque
Tlf = 1.1  #- torque load factor
Dt = (1*FT).asUnit(M)  #- ballast block moment arm
Acap = (1000*LBF).asUnit(N)  #- minimum 1/2" anchor bolt capacity
phiB = 0.9  #- ballast block weight phi factor
WtB = (750*LBF).asUnit(N)  #- Minimum weight of ballast block
DC_1_0 = Tlf * To_1 / (phiB * WtB * Dt)  #- Ballast  D/C ratio
DC_1_1 = Tlf * To_1 / (Acap * 1*FT)  #- Anchor bolt D/C ratio
#
# section: Long Term D/C Ratios
k_1 = (100*LBF/IN**3).asUnit(N/CM**3)  #- subgrade modulus
P_b = (2000 * PSF).asUnit(KPA)  #- allowable bearing pressure
COF = 0.56  #- dynamic COF with ground
FF = 1  #- friction factor
#
# section: Seismic Sliding Resistance
