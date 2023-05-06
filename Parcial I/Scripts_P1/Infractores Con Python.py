'''
La policía de tránsito de ciudad Gótica, debido a la gran cantidad de accidentes de tránsito 
ocurridos en los últimos meses por exceso de velocidad, decide dividir la ciudad en cuatro cuadrantes, 
teniendo cada cuadrante su propio límite de velocidad.
Para monitorear la velocidad a la cual circulan los vehículos se colocan 
cámaras y sensores de velocidad en varios puntos de los cuadrantes.
De cada vehículo se registra la placa y la velocidad que llevaba al ser monitoreado, en millas por hora.
Esta información se envía inmediatamenteal departamento de tránsito 
donde se genera para cada vehículo lo siguiente:

Placa del vehículo, Cuadrante por el cual circulaba (1, 2, 3 ó 4) y velocidad registrada (millas/hora)

Desarrolle una aplicación de consola VB2010 que procese la información anterior para un grupo de
vehículos y determine e imprima:

Para cada vehículo:
1. Indicar si es infractor o no, en caso de serlo, la multa en $ que debe pagar. (4 puntos)

Para todos los vehículos:
 Porcentaje de vehículos que circularon por el cuadrante 4 que no fueron infractores con respecto al total de vehículos reportados en ese cuadrante. (3 puntos)
3. Cuantos vehículos fueron procesados por el departamento de tránsito antes de encontrar al primer infractor. (2 puntos)
4. Promedio de dólares cancelados por concepto de multas. ( 2 puntos)
'''
#Ejercicio Elaborado Por Juan Jimenez 

#Declaracion de variables
placa=cuadrante=0
velocidadmilla=0.0
conversionmilla=0.0
dife=multa=0.0
contador1=contador2=contador3=0
acum=0
porcentaje=promedio=0.0
conversion2=0.0
total=0
total2=0

#variable para la condicion del ciclo while
resp="s"

#inicio del ciclo while
while resp.upper()=="S":
    #Entrada De Datos
    placa = int(input("Indique La Placa Del Conductor:"))
    cuadrante = int(input("Indique El Cuadrante (1)(2)(3)(4):"))
    velocidad = float(input("Indique La Velocidad (Milla/hora):"))

    if cuadrante == 1 or cuadrante == 2: # Condicion Para Indicar El Cuadrante
        conversionmilla = 1.61 * velocidad # Conversion millas a kilometros

        if conversionmilla > 80: # Condicion para ver si el conductor es infractor o no
            dife = conversionmilla - 80 # variable para encontrar los kilometros excedidos
            conversion2 = dife / 1.61 # Variable para saber cuantas millas se excedio
            multa = 2.5 * conversion2 # Multa del infractor
            acum += multa  # Variable que acumula el monto de las multas
            contador3 += 1  # Contador para saber el numero de conductores multados
            print("El Conductor Es Infractor, Debe Pagar Una Multa De: %.3f" %multa , "$")

        elif conversionmilla <= 80:
            total =+ 1 #Contador Para Ir Sumando La Cantidad de Vehiculos Que No Son Infractores
            print("El Conductor No Posee Multa ")

    if cuadrante == 3 or cuadrante == 4:  # Condicion Para Indicar El Cuadrante
        conversionmilla = 1.61 * velocidad # Conversion millas a kilometros
        if conversionmilla > 60: # Condicion para verificar si el conductor es infractor o no
            dife = conversionmilla - 60
            conversion2 = dife/ 1.61 # Variable para saber cuantas millas se excedio
            multa = 2.5 * conversion2#variable para saber la multa de l conductor
            acum += multa #Variable que acumula las multas]
            contador3 += 1 #Contador que suma los infractores
            contador2 += 1
            print("El Conductor Es Infractor, Debe Pagar Una Multa De: %.3f" %multa , "$")

        elif conversionmilla <= 60:
            total =+ 1 # Contador Para Ir Sumando La Cantidad de Vehiculos Que No Son Infractores
            contador1+=1 # contador para saber el porcentaje
            print("El Conductor No Posee Multa")

    resp = input("Desea Incluir Otra Persona? Si(s) / No(n):") #Respuesta para cerrar el ciclo o continuar

# Condicion Para Saber Si Hubo Infractores en el dia o no, Esto lo hice opcional para que no se indetermine
if contador2 <= 0:
    print("No Hubo Ningun Infractor En El Dia")
else:
    porcentaje = contador1/contador2 * 100
if contador3 <= 0:
    print("No Existe Ningun Promedio De Dolares En El Dia")
else:
    promedio= acum / contador3

print("***Resultador***")
print("El Porcentaje De Conductores Que No Fueron Infractores Es De: %2.f" % porcentaje, "%")
print("Hubo Un Total De:" , total, "Vehiculos Antes De Encontrar El Primer Infractor")
print("El Promedio Es De: %.2f" % promedio, "$")
