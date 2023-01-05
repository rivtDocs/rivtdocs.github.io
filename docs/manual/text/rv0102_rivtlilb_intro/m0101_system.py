"""
This file contains Python equations from the on-c-e model 
 m0101_system.txt

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
# section: Project Description
#
# section: AST Overview
#
# section: Track and Slew Drive Base
#
# section: A-frame, Arc Assembly, Z-purlin
#
# section: Drive System
#
# section: AST Terms and Definitions
