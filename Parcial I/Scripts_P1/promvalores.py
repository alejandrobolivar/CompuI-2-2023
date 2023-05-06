# Determinar el promedio de n números de un conjunto

# Lectura de datos
n = int(input('Indique la cantidad de elementos: '))

# Inicialización de variables
suma = 0

# Procesamiento de datos
for k in range(n):
    # Lectura de datos
    num = int(input('Indique un valor: '))
    suma = suma + num
prom = suma / n

# Salida de datos
print ('El promedio es: ', prom)

# Fin del programa
input('Pulse una tecla para finalizar... ')  # Pausa
