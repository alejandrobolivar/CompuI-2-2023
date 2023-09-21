# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 13:51:19 2023

@author: bolivar
"""
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

sym.var('x', real = True)

f = x ** 2
df = sym.diff(f, x)
print(df)
x_c = sym.solve(df, x)
print(x_c)
f_num = sym.lambdify([x], f, 'numpy')
x_vec = np.linspace(-5, 5, 100)


plt.plot(x_vec, f_num(x_vec))
plt.xlabel('$x$')
plt.ylabel('$x^2$')
plt.show()