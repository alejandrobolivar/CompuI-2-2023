'''
La guerra es un juego de cartas clásico, donde dos jugadores dividen una pila inicial
completa de cartas de manera uniforme. Cuando se inicia el juego, en cada ronda
ambos jugadores tiran una carta de su pila. El jugador con la carta más alta obtiene
todas las cartas de la ronda. Si los jugadores empatan, juegan de nuevo hasta que
un jugador gane la ronda o se acaben las cartas. El objetivo del juego es recoger la
mayor cantidad de cartas para ser el ganador.
Se dispone de dos archivos de datos “jugador1.txt” y “jugador2.txt”, donde se encuentra en cada uno, la pila de
cartas que le corresponde a cada jugador. Considere que cada archivo contiene:
En la primera línea de datos el Nombre del Jugador y a partir de la segunda línea,
cada una de las cartas que tiene en la pila.
Desarrolle un programa que procese la información de los archivos y genere el archivo
“resultados.txt” que contenga en cada línea el nombre del jugador que gana la ronda y cuantas cartas gana, en
caso de haber empate debe colocar la palabra guerra.
Además determine e imprima por consola:
1. Porcentaje de veces que hubo guerra en el juego. (2.5 puntos)
2. Nombre del Jugador ganador. (2.5 puntos)
Consideraciones:
a) La pila de cartas se dividió al inicio de manera uniforme, es decir, los dos jugadores tienen la misma cantidad de
cartas.
b) Se desconoce la cantidad de cartas que había en la pila inicial.
c) Si las cartas se acaban y termina la ronda en guerra, no se le asignan las cartas a ningún jugador.

# variables de entrada
jugador1: str
jugador2: str
carta1: int
carta2: int
# variables de salida
porc: float
# variables de proceso
contguerra: int = 0
controndas: int = 0
mazo: int
cartasJugador1: int
cartasJugador2: int
ganaronda: str
'''
contguerra = 0
controndas = 0
with open('jugador1.txt', 'r') as arch1:
    arch2 = open('jugador2.txt', 'r')
    arch3 = open('resultados.txt', 'w')
    # inicializaciones
    mazo = 0
    cartasJugador1 = 0
    cartasJugador2 = 0

    contenido1 = arch1.readlines()
    contenido2 = arch2.readlines()

    jugador1= contenido1[0].strip("\n")
    jugador2= contenido2[0].strip("\n")

    for i in range(1, len(contenido1)):
        controndas += 1

        carta1= int(contenido1[i])
        carta2= int(contenido2[i])

        mazo += 2
        if carta1 != carta2 :
            if carta1 > carta2 :
                ganaronda = jugador1
                cartasJugador1 += mazo
            else:
                ganaronda = jugador2
                cartasJugador2 += mazo

            arch3.write("Ronda %d : %s - %d\n" % (controndas, ganaronda, mazo))
            mazo = 0
        else:
            arch3.write("Ronda %d : Guerra\n" % controndas)
            contguerra += 1


    if controndas != 0:
        porc = contguerra / controndas * 100
        print(f"Porcentaje de veces que hubo guerra en el juego: {porc:.2f}%")
    else:
        print("No hubo juego")


    if cartasJugador1 > cartasJugador2:
        print(f"Ganador:  {jugador1}")
    elif cartasJugador1 < cartasJugador2:
        print(f"Ganador: {jugador2}")
    else:
        print("Empate")

arch2.close()
arch3.close()

print()
print("El Archivo Resultados.txt fue creado")
