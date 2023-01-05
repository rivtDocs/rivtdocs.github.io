"""
This file contains Python equations from the on-c-e model 
 m0401_aframe.txt

For interactive analysis open the file
in an Ipython Notebook or Komodo IDE interactive shell.

For interactive analysis in a Pyzo shell
open and run this file as a script. To execute the model
create a new Pyzo shell and put the following lines in
the starup script:

import os
os.system("python -m once " + __file__)
exit()

then open the model file, select new shell from shell menu 
and run.  The UTF calc can be opened and auto-reloaded.
""" 
from __future__ import division
from __future__ import print_function
import os
import sys
from sympy import *
from numpy import *
import numpy.linalg as LA
from collections import OrderedDict
sys.path.append('D:\\Egnyte\\Shared\\01_General\\03_Engineering\\05_Tracker\\14_EngDocs\\phase1\\ats_calcs_asce7')
try:
   from unum import Unum
except:
   print("unum module not found")
try:
   from once.calunit import *
except:
   print("calunit file not found in once script folder")


# begin equations
#
# section: A-frame and Connection Behavior
#
# section: AISI S100 Chapter F Tests and D/C Ratios
C_c = 1.52  #- calibration coefficient
M_m = 1.1  #- material factor
F_m = 1  #- fabrication factor
P_m = 1  #- professional factor
B_o = -3.5  #- reliability index
V_m = .06  #- material variation
V_f = .05  #- fabrication factor
C_p = 5.7  #- sample size factor
V_p = .065  #- test variation
V_q = .21  #- load effect
R_n = 9*KN  #- average of test results
phi = C_c*M_m*F_m*P_m*2.718**(B_o*(V_m**2 + V_f**2 + C_p*V_p**2+V_q**2)**.5)  #- Resistance factor
#
# section: Leg and Tie D/C Ratios
#
# section: Pivot Arm and Purlin Bracket D/C Ratios
#
# section: Arc Gear, Lock and Pinion Gear D/C Ratios
