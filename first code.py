# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 19:55:56 2021

@author: Avat pardaz
"""

import scipy.integrate as spi
import numpy as np
import pylab as pl

beta0=17/5
gamma=1/5.0
mu=1/(50*365.0)
S0=0.06
I0=0.001
E0 = 0.001
sigma = 1/8
ND=MaxTime=1000*365.0