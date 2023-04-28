'''
Su profesor de física le propuso un tema de investigación de campo que consiste
en estudiar y simular las trayectorias de los batazos de los jugadores de
beisbol. La idea fundamental es crear un programa que lea de un archivo de
datos de nombre stadium.txt , el cual contiene la información del stadium y los
batazos registrados en ese stadium. La información del archivo tiene la
siguiente estructura, en la primera línea la información del stadium:

Distancia del Home al Muro por el Center Field o Largo del Campo (m) y la
altura del Muro (m) y a continuación los datos de los batazos que se han
registrado en ese stadium, que consiste en:
Nombre del Bateador, Altura del Bateo (m), Velocidad de Salida (m/s) y ángulo
 de salida (expresado en grados)
Desarrolle un programa que lea la información del archivo stadium.txt y
genere un archivos de nombre jonrones.txt el cual debe contener los nombres de
los bateadores que batearon jonrón y otro de nombre otros.txt que debe contener
los nombres de los bateadores que conectan batazos que no son jonrón. Además
imprima por pantalla las siguientes estadísticas:
1. Porcentaje de Batazos de cada tipo(Ver consideraciones)
2. Nombre del Bateador, Velocidad y ángulo de salida del jonrón más largo

CONSIDERACIONES
a) Distancia Horizontal máxima de alcance (m), se calcula según la siguiente
fórmula:
Xmax = (Velocidad) ** 2 * sin(2 * Angulo) / 9.81
b) Altura del Batazo (m), se calcula según la siguiente la fórmula:
Y = AlturaBateo + Largo * tan(Angulo) - 9.81 * (Largo) ** 2 / (2 * (Velocidad) ** 2 * (cos(Angulo)) ** 2)
c) Los tipos de Batazo son:
Tipo de Batazo; Condición
Dentro del Cuadro; Xmax <= 36.88
En los Outfielders; (36.88 < Xmax < Largo del Campo) ó (Xmax > Largo Campo y
Altura del Batazo <= Altura del Muro)
Jonrón; Xmax > Largo Campo y Altura del Batazo > Altura del Muro
PI radian = 180°
d) g=9.81 m/s (aceleración de la gravedad terrestre)
'''
from math import sin, cos, tan, pi
# Entradas
Largo: float
Alto: float
Nomb: str = ""
AlturaBateo: float
Velocidad: float
Angulo: float
cent: int

# Salidas
PorcenJonron: float
PorcenOutfilders: float
PorcenDentro: float
NombMayor: str = ""
VelocidadMayor: float
AnguloMayor: float

# Procesos
ContJonron: int
ContOutfielders: int
ContDentro: int
Total: int
BandMayor: bool
Xmax: float
Y: float
XmaxMayor: float

# Registro de Archivos
arch1 = open("Stadium.txt", 'r')
arch2 = open("Jonrones.txt", 'w')
arch3 = open("Otros.txt", 'w')

# Zona 1:
# Inicializacion de Herramientas
BandMayor = True
ContDentro = 0
ContJonron = 0
ContOutfielders = 0
Total = 0

# Ciclo Externo
registro = arch1.readlines()
linea = 0

while linea < len(registro):
    lista_ext = registro[linea].split(',')
    linea += 1
    # Zona 2:
    # Lectura de Datos

    Largo = float(lista_ext[0])
    Alto = float(lista_ext[1])
    cent = 0
    # Ciclo Interno
    while cent == 0:
        # Zona 3:
        # Lectura de Datos
        lista_int = registro[linea].split(',')
        linea += 1
        Nomb = lista_int[0]
        AlturaBateo = float(lista_int[1])
        Velocidad = float(lista_int[2])
        Angulo = float(lista_int[3])

        # Calculos Pertinentes
        Angulo = Angulo * pi / 180  # Transformacion
        Xmax = (Velocidad) ** 2 * sin(2 * Angulo) / 9.81
        Y = AlturaBateo + Largo * tan(Angulo) - 9.81 * (Largo) ** 2 / (2 * (Velocidad) ** 2 * (cos(Angulo)) ** 2)

        if Xmax > Largo and AlturaBateo > Alto:
            arch2.write(f'{Nomb}\n')
            ContJonron += 1

            # p2. Obtencion del jonron mas largo
            if BandMayor:
                NombMayor = Nomb
                VelocidadMayor = Velocidad
                AnguloMayor = Angulo * 180 / pi
                XmaxMayor = Xmax
                BandMayor = False
            elif Xmax > XmaxMayor:
                NombMayor = Nomb
                VelocidadMayor = Velocidad
                AnguloMayor = Angulo * 180 / pi
                XmaxMayor = Xmax

        elif Xmax <= 38.88:
            arch3.write(f'{Nomb}\n')
            ContDentro += 1
        else:
            arch3.write(f'{Nomb}\n')
            ContOutfielders += 1

        Total += 1
        # Verificacion del ultimo
        cent = int(lista_int[4])

# Zona 5:
# Impresion de Resultados
if Total > 0:
    PorcenJonron = ContJonron / Total * 100
    PorcenDentro = ContDentro / Total * 100
    PorcenOutfilders = ContOutfielders / Total * 100

    print(f"Porcentaje de Batazos en Jonrones: {PorcenJonron:.2f}%")
    print(f"Porcentaje que Cayeron Dentro: {PorcenDentro:.2f}%")
    print(f"Porcentaje de Batazos en Outfielders: {PorcenOutfilders:.2f}%")
else:
    print("No Hubo Batazos")

if not BandMayor:
    print("Datos del Bateador con jonron mas largo:")
    print(f"Nombre: {NombMayor}; Velocidad: {VelocidadMayor:.2f}; Angulo: {AnguloMayor:.2f}")
else:
    print("No Hubo Jonrones")

arch1.close()
arch2.close()
arch3.close()