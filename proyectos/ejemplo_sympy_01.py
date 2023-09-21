'''
Ley de Gas Ideal

'''

import sympy as sym


P, V, n, R, T = sym.symbols('P V n R T')

# Gas constont
R = 8.314  # J/K/gmoL
R *= 1000  # J/K/kgmoL

# Moles of air
mAir = 1  # kg
mwAir = 28.97  # kg/kg-moL
n = mAir/mwAir

# Temperatura
T = 298

# Equation
eqn = sym.Eq(P*V, n*R*T)

# Solve for P
f = sym.solve(eqn, P)
print(f[0])

# Use the sympy pLot function to plot
sym.plot(f[0], (V, 1, 10), xlabel='Volume m**3', ylabel='Pressure Pa')

