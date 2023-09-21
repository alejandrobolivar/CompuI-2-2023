# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 16:54:23 2023

@author: bolivar
"""
from sympy import symbols, sin, cos, pi
from sympy. plotting import plot3d_parametric_surface

x, y = symbols ('x y')
plot3d_parametric_surface ((2- cos(x))*cos(y) ,(2-cos(x))*sin
(y),sin(x) ,(x ,0 ,2* pi) ,(y ,0 ,2* pi))