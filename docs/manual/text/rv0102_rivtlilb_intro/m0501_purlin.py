"""
This file contains Python equations from the on-c-e model 
 m0501_purlin.txt

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
# section: Z-Purlin Properties
#
# section: Z-Purlin D/C Ratios
#
# section: Panel Clamps
#
# section: Panel Deflection D/C Ratio
#
# section: Drive Tube and Coupler D/C Ratios
