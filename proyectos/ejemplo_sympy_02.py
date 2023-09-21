# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 07:17:18 2023


DADO:
Un peso de 22 libras se cuelga de un anillo. El anillo está sostenido por 
dos cuerdas. La primera cuerda, cuerda CE, está 30 grados por encima de la 
horizontal ya la derecha. La segunda cuerda, cuerda BD, está 45 grados a la 
izquierda y por encima de la horizontal.

w = 22 lb

TCE @ +30 degrees CCW relative to +x-axis

TBD @ +45 degress CW relative to -x-axis

FIND:

The magnitude of TCE
and TBD

@author: bolivar
"""

import numpy as np
from sympy import symbols, Eq, solve

Tce, Tbd = symbols('Tce Tbd')

eq1 = Eq(Tce * np.cos(np.radians(30)) - Tbd * np.cos(np.radians(45)))
print(eq1)

eq2 = Eq(Tce * np.sin(np.radians(30)) + Tbd * np.sin(np.radians(45))-22)
print(eq2)

sol_dict = solve((eq1, eq2), (Tce, Tbd))
print(f'Tce = {sol_dict[Tce]}')
print(f'Tbd = {sol_dict[Tbd]}')

