# Lectura de datos
x = float(input('Ingrese un valor x: '))

# Procesamiento de datos
if x < 0.0:
	msg = 'negativo'
elif x > 0.0:
	msg = 'positivo'
else:
	msg = 'cero'

# Salida de datos
print ('x es ', msg)

# Fin del programa
input('Pulse una tecla para finalizar... ') # Pausa
