'''
M I C K E Y V I R T U A L E N D I S N E Y
En el Parque de diversiones de Disney, hay un juego que es muy popular entre los niños que
visitan el mismo, llamado pinta a Mickey, el cual consiste en disparar al rostro de Mickey con
un láser de colores virtual. Para ello, los niños apuntan con una pistola el rostro de Mickey y
esta acción hace que la computadora registre las coordenadas X, Y del punto del disparo.
El primero en acertar la nariz ((x ** 2 + (y + 4) ** 2) = 0.5 ** 2) de Mickey obtiene un premio, pero sólo el primero. 
Desarrolle un programa que, dados los datos registrados de un día de en el
parque de diversiones, determine:
a) Porcentaje de puntos que quedan ubicados en alguna oreja 
(OD (X + 3) ** 2 + Y ** 2 = 4, OI (X – 3) ** 2 + Y ** 2 = 4).
b) Promedio de las coordenadas X de los puntos ubicados dentro de la cara de Mickey.
c) Un mensaje que indique si hubo o no ganador de premio ese día.
'''

# Inicializaciones
cent = 0
band = 0
cont_total = 0
cont_oreja = 0
acum_cara = 0
cont_cara = 0
nombre = ""

while cent == 0:

    # Lectura de variables
    Nombre = input("Ingrese el nombre del jugador: ")
    x = input("Ingrese la coordenada X: ")
    y = input("Ingrese la coordenada Y: ")

    # Contador total de jugadores
    cont_total += 1

    # Pregunta a
    # Contador para el porcentaje de disparos ubicados en alguna oreja
    if (((x + 3) ^ 2 + y ^ 2) <= 4 and (x ^ 2 + (y + 3) ^ 2) > 9) or \
    (((x - 3) ^ 2 + y ^ 2) <= 4 and (x ^ 2 + (y + 3) ^ 2) > 9):
        cont_oreja += 1

    # Pregunta b
    # Acumulador y contador para el promedio de las coordenadas X de los disparos ubicados dentro de la cara de Mickey
    if (x ^ 2 + (y + 3) ^ 2) <= 9 and (x ^ 2 + (y + 4) ^ 2) > 0.25:
        acum_cara += x
        cont_cara += 1

    # Pregunta c
    # Nombre del ganador (disparo en la nariz)
    if band == 0 and (x ^ 2 + (y + 4) ^ 2) <= 0.25:
        band = 1
        nombreganador = nombre

    cent = input("¿Existe otro jugador? (SI:0  NO:1): ")

# Impresión pregunta a
if cont_total != 0:
    porcentaje = cont_oreja / cont_total * 100
    print("Porcentaje de jugadores que su disparo quedó ubicado en una de las orejas: " , porcentaje , "%")
else:
    print("No hubo jugadores")

# Impresión pregunta b
if cont_cara != 0:
    promedio = acum_cara / cont_cara
    print("Promedio de las coordenadas X de los puntos ubicados dentro de la cara: {promedio:6.2f}")
else:
    print("Ningún jugador disparó a la cara de Mickey")

# Impresión pregunta c
if band != 0:
    print(nombreganador , " fue el ganador del día, ¡FELICIDADES!")
else:
    print("No hubo ganador")