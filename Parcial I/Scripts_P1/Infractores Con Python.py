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

Desarrolle un programa que procese la información anterior para un grupo de
vehículos y determine e imprima:

Para cada vehículo:
1. Indicar si es infractor o no, en caso de serlo, la multa en $ que debe pagar.

Para todos los vehículos:
2. Porcentaje de vehículos que circularon por el cuadrante 4 que no fueron infractores 
con respecto al total de vehículos reportados en ese cuadrante.
3. Cuantos vehículos fueron procesados por el departamento de tránsito antes de encontrar al primer infractor.
4. Promedio de dólares cancelados por concepto de multas. 
Consideraciones:
a) Los límites de velocidad son:
 80 km/hora para los cuadrantes 1 y 2
 60 km/hora para los cuadrantes 3 y 4
b) La multa a pagar será de 2.50 $ por cada milla/hora que se excedió la
velocidad límite.
c) Una milla/hora equivale a 1,61 km/hora.
'''

placa = cuadrante = 0
velocidadmilla = 0.0
conversionmilla = 0.0
dife = multa = 0.0
contador1 = contador2 = contador3 = 0
acum = 0
porcentaje = promedio = 0.0
conversion2 = 0.0
total = 0
total2 = 0

#variable para la condicion del ciclo while
resp = "s"

#inicio del ciclo while
while resp.upper() == "S":
    #Entrada De Datos
    placa = input("Indique La Placa Del Conductor:")
    cuadrante = int(input("Indique El Cuadrante (1)(2)(3)(4):"))
    velocidad = float(input("Indique La Velocidad (Milla/hora):"))
        
    if cuadrante == 1 or cuadrante == 2: # Condicion Para Indicar El Cuadrante
        conversionmilla = 1.61 * velocidad # Conversion millas a kilometros

        if conversionmilla > 80: # conductor es infractor
            dife = conversionmilla - 80  # variable para encontrar los kilometros excedidos
            conversion2 = dife / 1.61  # Variable para saber cuantas millas se excedio
            multa = 2.5 * conversion2  # Multa del infractor
            acum += multa  # Variable que acumula el monto de las multas
            contador3 += 1  # Contador para saber el numero de conductores multados
            print("1) El Conductor Es Infractor, Debe Pagar Una Multa De: %.3f" % multa , "$")

        else:
            
            print("1) El Conductor No Posee Multa ")

    else:  # Cuadrantes 3 o 4
        conversionmilla = 1.61 * velocidad # Conversion millas a kilometros
        if conversionmilla > 60: # Conductor es infractor
            dife = conversionmilla - 60 
            conversion2 = dife / 1.61  # cuantas millas se excedio
            multa = 2.5 * conversion2  # multa del conductor
            acum += multa  # Variable que acumula las multas]
            contador3 += 1  # Contador que suma los infractores
            print("1) El Conductor Es Infractor, Debe Pagar Una Multa De: %.3f" %multa , "$")

        else:
            
            if cuadrante == 4:
                contador1 += 1 # contador para saber el porcentaje
            print("1) El Conductor No Posee Multa")
        if cuadrante == 4:
            contador2 += 1
    
    if contador3 == 0:  # No se ha encontrado el primer infractor
        total =+ 1
    
    resp = input("Desea Incluir Otra Persona? Si(s) / No(n):") #Respuesta para cerrar el ciclo o continuar

# Condicion Para Saber Si Hubo Infractores en el dia o no, Esto lo hice opcional para que no se indetermine
if contador2 <= 0:
    print("No Hubo Ningun Infractor En El Dia")
else:
    porcentaje = contador1 / contador2 * 100
    print("2) El Porcentaje De Conductores Que No Fueron Infractores es= %2.f" % porcentaje, "%")

print("3) Hubo Un Total De:" , total, "Vehiculos Antes De Encontrar El Primer Infractor")

if contador3 <= 0:
    print("No hubo multas")
else:
    promedio = acum / contador3
    print("4) El Promedio cancelado por concepto de multas= %.2f" % promedio, "$")
