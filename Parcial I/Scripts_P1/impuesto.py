# Lectura de datos
sueldo = float(input('Ingrese su sueldo: '))

# Procesamiento de datos
if sueldo < 1000:
	tasa = 0.00
elif sueldo < 2000:
	tasa = 0.05
elif sueldo < 4000:
	tasa = 0.10
else:
	tasa = 0.12

# Salida de datos
print ('Usted debe pagar ', tasa * sueldo, ' de impuesto')

# Fin del programa
input('Pulse una tecla para finalizar... ') # Pausa

