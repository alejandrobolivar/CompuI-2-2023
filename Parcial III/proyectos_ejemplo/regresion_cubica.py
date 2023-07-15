'''
 Regresión cúbica. Con los siguientes datos de Cp del propano vs temperatura,
obtenga los coeficientes de la ecuación de Cp de la forma.
Cp = a + bT + cT**2 + dT**3
Temp(C)     50      100     150     200     273.16  298.15  300     400
Cp(kJ/kg)   34.06   41.3    48.79   56.07   68.74   73.6    73.93   94.01 . . .

Temp(C)     500     600     700     800     900     1000    1100
Cp(kJ/kg)   112.59  142.67  154.77  163.35  174.6   182.67  128.7

Aplique la regresión cúbica para obtener los coeficientes a, b, c, d.

Solución
La temperatura es la variable independiente x, y el Cp es la variable dependiente y.

'''

import numpy as np
import matplotlib.pyplot as plt

x = np.array ([50, 100, 150, 200, 273.16, 298.15, 300, 400, 500, 600,\
700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500])
y = np.array ([34.06, 41.3, 48.79, 56.07, 68.74, 73.6, 73.93, 94.01,\
112.59, 128.7, 142.67, 154.77, 163.35, 174.6, 182.67,\
189.74, 195.85, 201.21, 205.89])

xs = np.linspace(50, 1500, 100)

p = np.polyfit(x, y, 3)
print(p)
# fig = plt . figure ()
plt.scatter(x, y, label = 'Datos')
plt.plot(xs, np.polyval(p, xs), ':r', label = 'Interpolacion cúbica')
plt.xlabel('Temperatura')
plt.ylabel('Cp')
plt.legend()
plt.title('Cp del propano')
plt.grid()
plt.show()
# fig.savefig("regcubi.pdf", bbox_inches = ' tight ')
# Por lo tanto, la ecuación del Cp del propano es
# Cp = −1.51288977e − 08 T**3 − 2.68480214e − 05 T**2 + 1.96470716e − 01 T + 2.05235040e + 01