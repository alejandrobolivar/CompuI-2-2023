# Lectura de datos
agrado = float(input('Ingrese el valor de agrado: '))

# Procesamiento de datos
if agrado <= 20:
	msg = 'Muy Malo'
elif agrado <= 40:
	msg = 'Deficiente'
elif agrado <= 60:
	msg = 'Regular'
elif agrado <= 80:
	msg = 'Bueno'

else:  # Observe que no es necesario hacer la última pregunta
	msg = 'Muy Bueno'

# Salida de datos
print ('La Calificación es ' + msg)

# Fin del programa
input('Pulse una tecla para finalizar... ') # Pausa

