"""
This file contains Python equations from the on-c-e model 
 m0401_components.txt

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
# section: A-frame Assembly Tests - S100 Chapter F
C_c = 1.52  #- calibration coefficient
M_m = 1.1  #- material factor
F_m = 1  #- fabrication factor
P_m = 1.0  #- professional factor
V_m = .06  #- material variation
V_f = .05  #- fabrication factor
V_p = .065  #- test variation
V_q = .21  #- load effect
B_o = 2.5  #- reliability index
n4 = 4  #- sample size
n6 = 6  #- sample size
C6_P =  (1+1/n6)*(n6-1)/(n6-3)  #- Sample size correction factor n=6
phi6 = C_c*M_m*F_m*P_m*2.718**(-B_o*(V_m**2 + V_f**2 + C6_P*V_p**2+V_q**2)**.5)  #- Resistance factor - sample size n=6
C4_P =  (1+1/n4)*(n4-1)/(n4-3)  #- Sample size correction factor n=4
phi4 = C_c*M_m*F_m*P_m*2.718**(-B_o*(V_m**2 + V_f**2 + C4_P*V_p**2+V_q**2)**.5)  #- Resistance factor - sample size n=4
#
# section: A-frame Assembly Tests - D/C Ratios
F_0 = 1.8 * KN  #- from [0202][3] Table 3.2
M_0 = 0.9 * KN *M  #- from [0202][3] Table 3.2
F_20 = 1.5 * KN  #- from [0202][3] Table 3.2
M_20 = 1.4 * KN *M  #- from [0202][3] Table 3.2
DC0_F = F_0 / (2.7 * KN)  #- Force D/C - 0 deg stow
DC0_M = M_0 / (1.4 *KN*M)  #- Moment D/C Ratio - 0 deg stow
DC20_F = F_20 / (3.2 * KN)  #- Force D/C Ratio Operation - 20 deg
DC20_M =  M_20 / (1.6 * KN * M)  #- Moment D/C Ratio - Operation with dynamics- 20 deg
#
# section: Leg, Tie, Pivot Arm D/C
Pcomp_1 = 1.5 *KN  #- maximum compression in leg
Myy_1 = 0.2*KN*M  #- maximum moment at tie
Vx_1 = 0.5*KN  #- maximum shear at tie
Pcomp_2 = .9 * KN  #- maximum compression in tie
Myy_2 = 0.2 * KN*M  #- maximum moment at tie
Vx_2 = .8*KN  #- maximum shear at tie
Pcomp_3 = 100*LBF  #- maximum compression arm
Myy_3 = 2800*IN*LBF  #- maximum moment in arm
Vx_3 = 130*LBF  #- maximum shear in arm
