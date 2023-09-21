# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 07:17:18 2023

@author: bolivar
"""

import numpy as np
from sympy import symbols, Eq, solve

w, Tce, Tbd = symbols('w, Tab, Tac')


eq1 = Eq(Tce * np.cos(np.radians(30)) - Tbd * np.cos(np.radians(45)))
print(eq1)
eq2 = Eq(Tce * np.sin(np.radians(30)) + Tbd * np.sin(np.radians(45))-w)
print(eq2)
sol_dict = solve((eq1, eq2), (Tce, Tbd))

print(f'Tce = {sol_dict[Tce]}')
print(f'Tbd = {sol_dict[Tbd]}')
