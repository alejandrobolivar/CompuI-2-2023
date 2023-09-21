# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 19:44:39 2023

@author: bolivar
"""

from sympy.parsing.sympy_parser import parse_expr

a=input("Cualquier cosa: ")

t=parse_expr(a)

print(t)# y te saldrá en codigo sympy.
