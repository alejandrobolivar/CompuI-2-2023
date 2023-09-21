# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 20:32:05 2023

@author: bolivar

Una viga de 8 metros de longitud se le aplica una carga distribuida constante de 10 KN/m
desde la mitad de la viga hasta el final. Hay dos soportes simples debajo de la viga,
uno en el punto inicial y otro en el punto final de la viga, una carga puntual
de magnitud 5 KN también se aplica desde la parte superior de la viga, a una distancia de 4 metros
desde el punto de partida. Tome E = 200 GPa e I = 400*(10**-6) metro**4.
Usando la convención de signos de que las fuerzas hacia abajo son positivas.

"""
from sympy.physics.continuum_mechanics.beam import Beam
from sympy import symbols
R1, R2 = symbols('R1, R2')
b = Beam(8, 200*(10**9), 400*(10**-6))
b.apply_load(5000, 4, -1)
b.apply_load(R1, 0, -1)
b.apply_load(R2, 8, -1)
b.apply_load(10000, 4, 0, end=8)
b.bc_deflection = [(0, 0), (8, 0)]
b.solve_for_reaction_loads(R1, R2)
axes = b.plot_loading_results()
