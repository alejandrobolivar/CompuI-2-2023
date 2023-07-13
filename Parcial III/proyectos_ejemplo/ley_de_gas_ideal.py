'''
Ley de Gas Ideal

'''
import sympy as sp

P, V, n, R, T = sp.symbols('P, V, n, R, T')

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
eqn = sp.Eq(P*V, n*R*T)

# Solve for P
f = sp.solve(eqn, P)
print(f[0])

# Use the sympy pLot function to plot
sp.plot(f[0], (V, 1, 10), xlabel='Volume m**3', ylabel='Pressure Pa')
