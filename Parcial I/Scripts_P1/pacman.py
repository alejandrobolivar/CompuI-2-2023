'''
El famoso buscador Google ha querido celebrar el 30 aniversario de Pac Man transformando
su logo en un videojuego interactivo que el usuario puede utilizar moviendo las flechas de su teclado.
Este minijuego cuenta con todas las funciones del proyecto original: desde la música y los enemigos,
hasta los 256 niveles desarrollados por la empresa japonesa Namco. La
cabecera de la página del buscador se convierte en la tradicional pantalla del videojuego
aunque en esta ocasión es alargada y las paredes forman la palabra "Google".
La reacción de los fanáticos de este juego no se hizo esperar y Google detecto que los mismos
destinaban horas para entretenerse con PacMan. Para continuar la celebración,
Google decidió premiar a los mejores jugadores, para ello,
registra para cada una de las personas que jugaron:

Nombre del jugador, país de residencia, sexo del jugador, tiempo que duró jugando, puntaje obtenido

En base a la información anterior, desarrolle una aplicación de consola en VB2008 que determine e imprima:
1. Nombre y país del jugador que obtuvo el mejor puntaje.
2. Cantidad total de jugadores que participaron.
3. Porcentaje de jugadores que duraron más de 120 minutos jugando.
4. Puntaje promedio obtenido por los jugadores.
5. Nombre de la primera persona que duro menos de 40 minutos jugando.
6. Puntaje promedio obtenido por los jugadores de sexo femenino.
'''
nombre_40 = ""
acumpuntajef = 0
acumpuntaje = 0
puntajemejor = 0
cent = 0
band = 0
totalparticipantes = 0
cont_120 = 0
acumpuntaje = 0
band2 = 0
contf = 0
AcumPuntajeF = 0

while cent == 0:
    nombre = input("Ingrese el nombre del jugador: ")
    pais = input("Ingrese el paìs de residencia: ")
    sexo = input("Indique el sexo del jugador (M = Masculino, F = Femenino): ")
    tiempodejuego = int(input("Ingrese el tiempo que duró jugando en minutos: "))
    puntaje = int(input("Indique el puntaje obtenido: "))

    totalparticipantes += 1

    acumpuntaje += puntaje

    if band == 0:
        puntajeMejor = puntaje
        nombremejor = nombre
        paismejor = pais
        band = 1
    elif puntaje > puntajemejor:
        puntajeMejor = puntaje
        nombreMejor = nombre
        paismejor = pais

    if tiempodejuego > 120:
        cont_120 += 1

    if band2 == 0 and tiempodejuego < 40:
        band2 = 1
        nombre_40 = nombre

    if sexo.upper() == "F":
        acumpuntajef += puntaje
        contf += 1

    cent = int(input("Otro jugador [SI:0 / NO:1]:"))

if band != 0:
    print("1) El mejor puntaje los obtuvo %s y su pais de residencia es %s" % nombremejor, paismejor)
    print("2) Cantidad total de jugadores que participaron: " , totalparticipantes)
else:
    print("No hubo participantes")

if totalparticipantes != 0 and cont_120 != 0:
    porc_120 = (cont_120 / totalparticipantes) * 100
    print("3) Porcentaje de jugadores que duraron más de 120 minutos jugando: " , porc_120)
elif cont_120 == 0 and totalparticipantes != 0:
    print("Ningún participante jugó por más de 120 minutos")

if totalparticipantes != 0:
    puntajeprom = acumpuntaje / totalparticipantes
    print("4) Puntaje promedio obtenido por los jugadores: " , puntajeprom)

if band2 != 0:
    print("5) Nombre de la primera persona que duró menos de 40 minutos jugando: " , nombre_40)
else:
    print("Ningún jugador duró menos de 40 minutos jugando")

if contf != 0:
    puntajepromf = acumpuntajef / contf
    print("6) Puntaje promedio obtenido por los jugadores de sexo femenino: " , puntajepromf)
elif totalparticipantes != 0:
    print("No hubo jugadores de sexo femenino")