# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 16:54:23 2023

@author: bolivar
"""
from sympy import symbols, sin, cos, pi
from sympy. plotting import plot3d_parametric_line

x, y = symbols ('x y')
plot3d_parametric_line (x*cos (4*x),x*sin (4*x),x,(x,-2*pi ,2*
pi))