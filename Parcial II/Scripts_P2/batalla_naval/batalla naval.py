'''
El último deseo de Timmy Turner fue jugar Batalla Naval con barcos de verdad, y
sus padrinos magicos cumpliendos con su deber, se lo concedieron. Una vez
iniciada la batalla Timmy comenzó a disparar misiles a diestra y siniestra contra
la flota enemiga, pero debido a su poca inteligencia, Timmy no tomaba en
cuenta la cinematica del lanzamiento de proyectiles y a veces acertaba y otras
veces no.
Esto obligo a Timmy a desear un ingeniero que lo ayudara con el problema;
como resultado del deseo apareció usted.
El problema es el siguiente: el centro de control del barco de Timmy registra los
siguientes datos sobre los barcos de la flota enemiga:
IDENTIFICACIÓN, DISTANCIA DE DICHO BARCO AL BARCO DE TIMMY (EXPRESADO EN METROS) Y VELOCIDAD INICIAL HORIZONTAL
(V0X) DEL MISIL QUE TIMMY LANZÓ CONTRA ÉL (EXPRESADO EN M/S)
Usted debe desarrollar un programa que lea los datos registrados por el centro de control, en el archivo
LANZAMIENTOS.DAT y usando la teoría del lanzamiento de proyectiles:

Procese la información y determine e imprima por pantalla:
• De los barcos destruidos, la identificación del barco que estaba más cerca.
• De los barcos que NO fueron destruidos, porcentaje de misiles que no alcanzaron al barco enemigo
expresado respecto al total de barcos No destruidos.
• Porcentaje de barcos destruidos.
• Velocidad inicial vertical (V0Y) promedio en m/s.
CONSIDERACIONES
• Timmy disparó un misil por cada barco enemigo.
• La velocidad inicial (V0) es un dato proporcionado por el manual del lanzamisiles, el cual especifica que la
velocidad inicial del primer lanzamiento es de 250 m/s, y por cada nuevo lanzamiento disminuye 1%.
• Formulas necesarias:
alvance=vox*tvuelo, tvuelo=2voy/g, vo=(vox+voy)**0.5
'''

from math import sqrt

# inicializacion
c1=0
Acum=0
c3=0
c2=0
Vo=250
g=9.8
band=0

# apertura de archivos
arch1=open('lanzamientos.txt','r')
arch2=open('destruidos.txt','w')
arch3=open('nodestruidos.txt','w')

# Procesar el archivo
for registro in arch1:
	linea = registro.split(',')
	ID = linea[0]
	print(ID)
	Dentrebarcos = float(linea[1])
	print(Dentrebarcos)
	Vox = float(linea[2])
	print(Vox)

	Voy = sqrt(Vo**2 - Vox**2)
	Acum += Voy
	tvuelo = 2 * Voy / g
	alcance = Vox * tvuelo
	Vo = 0.99 * Vo
	Tiro = Dentrebarcos - alcance
	absoluto = abs(Tiro)

	if absoluto < 10**-3 :
		arch2.write(ID + '\n')
		c1 += 1
		if band == 0:
			menordistancia = Dentrebarcos
			IDmenor = ID
			band=1
		elif Dentrebarcos < menordistancia :
			menordistancia = Dentrebarcos
			IDmenor = ID
	else:
		c3 += 1
		print('No se destruyeron los barcos')
		if alcance < Dentrebarcos :
			c2 += 1
			arch3.write(ID+'\n')
		elif alcance>Dentrebarcos :
			arch3.write(ID +'\n')

arch1.close()
arch2.close()
arch3.close()

if band == 1:
	print('el ID del barco con la menor distancia es: ', IDmenor)
else:
	print('No se puede decir cual es el barco con menor distancia')

if c3 > 0:
	Porc = (c2 / c3) * 100
	print('El porcentaje de misiles q no alcanzaron al barco es de: ', Porc)
else:
	print('todos los misiles sobrepasaron el barco')

if c3 > 0:
	PorcD = (c1 / (c1 + c3)) * 100
	print('El porcentaje de barcos destruidos es de: ', PorcD)
else:
	print('Ningun barco fue destruido')

if (c1 + c3) > 0:
	prom = Acum / (c1 + c3)
	print('El promedio de la velocidad inicial en Voy es de:  ', prom)
else:
	print('No se procesaron barcos')