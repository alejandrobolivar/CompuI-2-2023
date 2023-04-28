#Inicializacion de variables
c1=0
acumt = 0
Asignado=False
Band=0
cr=0
c3=0
#Apertura de Archivos
arch1=open('Participantes.txt', 'r')
arch2=open('Completos.txt', 'w')
arch3=open('Incompletos.txt', 'w')

for registro in arch1:
	linea = registro.split(',')
	print(linea)
	lugarP = linea[0]
	print(lugarP)
	nombre = linea[1]
	print(nombre)
	edad = linea[2]
	print(edad)
	tseg = int(linea[3])
	print(tseg)
	kmalczd = int(linea[4])
	print(kmalczd)
	if kmalczd == 42:
		arch2.write(nombre + ',' + str(tseg) + '\n')
		acumt += tseg
		c1= c1 + 1

		if not(Asignado):
			completoM = kmalczd
			Primero = nombre
			Asignado = True
		elif kmalczd > completoM:
			Primero=nombre

		if Band == 0:
			MayorR=tseg
			nombremayor=nombre
			paismayor=lugarP
			Band= 1
		elif tseg > MayorR:
			MayorR = tseg
			nombremayor=nombre
			paismayor=lugarP
			cr=0
		elif tseg == MayorR:
			cr += 1

	else:
		arch3.write(nombre + ',' + str(kmalczd) + '\n')
		c3 += 1

arch1.close()
arch2.close()
arch3.close()
if Band != 0:
	print('La persona con el mejor recor es: ', nombremayor )
else:
	print('Nadie tuvo un record')
tprom = acumt / c1
if acumt > 0 :
	print('el tiempo promedio es : ' , tprom)
else:
	print('Nadie termino el maraton')
print('El primer participante en terminar el maraton fue: ' , Primero)
Porc = (c3 / c1) * 100
if c3 > 0:
	print('el porcentaje de participantes que no completaron el recorrido es de: ',  Porc)
else:
	print('Todos completaron la carrera')