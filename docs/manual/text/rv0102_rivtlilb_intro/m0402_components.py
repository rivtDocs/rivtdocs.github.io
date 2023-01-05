"""
This file contains Python equations from the on-c-e model 
 m0402_components.txt

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
# section: Z-Purlin Loads and Stabililty
#
# section: Z-Purlin Properties and D/C Ratios
#
# section: Z-Purlin Tests - S100 Chapter F
#
# section: Drive Tube, Coupler, Arc-gear D/C Ratios
torq_u = (64 * FT*LBF).asUnit(N*M)  #- maximum tube torque
tube_d = (2 * IN).asUnit(MM)  #- tube diameter
f_y_1 = (30 * KSI).asUnit(MPA)  #- bolt yield strength
g_u_1 = (10 * KSI).asUnit(MPA)  #- bolt shear strength
area1_b = (.2 * IN**2).asUnit(MM**2)  #- bolt cross section
S1_b1 = (.012 * IN**2).asUnit(MM**2)  #- bolt section modulus
tube_t = (.045 *IN).asUnit(MM)  #- tube thickness
slider_w = (1*IN).asUnit(MM)  #- slider width
COF1 = 1  #- COF between slider and bolt
shear1_u = torq_u / tube_d  #- bolt shear force
axial1_u = shear1_u * COF1  #- second order axial load
dc_7 = (axial1_u / area1_b) * (1/f_y_1)  #- axial stress D/C ratio
dc_8 = (shear1_u/ area1_b) * (1 / g_u_1)  #- shear stress D/C ratio
dc_9 = dc_8 + dc_7  #- stress interaction equation
bstress1 = shear1_u / (tube_t * slider_w)  #- bearing stress at slider
#
# section: Panel Deflection and Clamp D/C Ratios
#
# section: Fastener D/C Ratios
