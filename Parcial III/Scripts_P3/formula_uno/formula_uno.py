# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 16:21:05 2022
@author: Alejandro Bolívar

E S C E N A R I O
La Fórmula 1, conocida también como F1, es la competencia
internacional más popular de carros de carreras. Cada carrera se
denomina Gran Premio y la competición que las agrupa se denomina
Campeonato Mundial de Fórmula 1. Las carreras de Fórmula 1 se celebran
en circuitos urbanos o en circuitos especialmente construidos.
Con la finalidad de registrar posibles cambios en las estrategias de las
escuderías por cada corredor participante se le realiza el siguiente registro
en el archivo de nombre “carrera.txt”, Almacenándose la información
correspondiente a la ultima carrera de Formula 1 que este disputó, de la
siguiente manera: en la primera línea se almacena la información
del nombre del circuito, nombre del piloto y la hora de inicio de la carrera.
Adicionalmente, por cada vuelta realizada al circuito se toma: el tiempo de duración de la vuelta
(expresado minutos, segundos y centésimas de segundos), el tiempo de demora en el Pit
Stop expresado en segundos, así como la cantidad de llantas sustituidas.
Problema
Se requiere que diseñe una aplicación en VB2010 bajo consola, que procese la
información del archivo antes mencionado que determine e imprima por pantalla:
• Cantidad de veces que entró al Pit Stop el piloto. (Tiempo en Pit Stop>0)
• Hora de culminación de la competencia por el piloto, expresada en hora y minuto.
• La mejor vuelta realizada por el piloto (el tiempo que duro su vuelta mas rápida).

CONSIDERACIONES
1.- La hora de inicio de la carrera se encuentra en formato de hora militar, horas y minutos.
2.- En el archivo sólo se registran las vueltas completas al circuito por un solo piloto.
3.- No necesariamente el vehículo culmina la carrera.
4.- Si no entra al Pit Stop en el archivo se coloca como tiempo de parada 0 seg.
Por supuesto si no entra al Pit
Stop, no se le cambian llantas (Cero llantas).
La conversión de tiempo son: 1 hora = 60 Min, 1Min = 60 Seg, 1Seg. = 1000 Cseg.

Requerimientos
1.- Un subprograma que dado los datos de un tiempo en minutos, segundos y centésimas de segundo lo
transforme en centésimas de Segundos totales.
2.- Un subprograma que dado dos datos tiempos expresados en minutos, segundos y centésimas de
segundo, devuelva el tiempo menor.
3.- Cualquier otro tipo de subprograma que crea necesario realizar para que el procedimiento Main sea
de forma los más modular posible.

carrera.txt
Turquia, José Corredor, 7, 10
1, 40, 112, 0, 0
1, 25, 953, 0, 0
1, 40, 855, 0, 0
1, 35, 942, 0, 0
1, 29, 672, 18, 4
1, 36, 639, 0, 0
1, 46, 539, 0, 0
1, 43, 784, 0, 0

Cálculos a desarrollar (tiempo en centésimas de segundo de cada vuelta)
100112
85953
100855
95942
107672
96639
106539
103784
797496 <- Tiempo total Cseg

Ejecución:
Circuito:  TURQUIA
Piloto:  JOSE CORREDOR
Duración de la Carrera: Min Seg Cseg
13 17 496
Hora de finalizacion
7 23
Tiempo más rápido
1 25 953
Entradas a pit Stop
1
"""

# SP que dado los datos de un tiempo en minutos, segundos y centésimas de segundo lo
# transforme en centésimas de Segundos totales.
def transformar(minutos, seg, cseg):
    return (minutos * 60000) + (seg * 1000) + cseg

# SP que transforma centésimas de segundos totales a minutos, segundos y centésimas de segundo
def devolucion(cst):
    minutos = cst // 60000
    seg = (cst % 60000) // 1000
    cseg = cst % 1000
    return minutos, seg, cseg

# SP que dado dos datos tiempos expresados en minutos, segundos y centésimas de
# segundo, devuelve el tiempo menor.
def menor(min1, seg1, cseg1, min2, seg2, cseg2):
    csa = transformar(min1, seg1, cseg1)
    csb = transformar(min2, seg2, cseg2)
    if csa < csb:
        csm = csa
    elif csa > csb:
        csm = csb
    minutos, seg, cseg = devolucion(csm)
    return  minutos, seg, cseg

# SP de lectura de los datos de una vuelta
def leer(registro):
    linea = registro.split(',')
    minutos = int(linea[0])
    seg = int(linea[1])
    cseg = int(linea[2])
    segpit = int(linea[3])
    cauchos = int(linea[4])
    return minutos, seg, cseg, segpit, cauchos

# SP que suma dos horas expresadas en hh:min
def sumahora(hi, mi, minutos):
    if minutos > 60:
        mf = mi + minutos % 60
        hf = hi + minutos // 60
    else:
        mf = mi + minutos
        hf = hi
    return  hf, mf

def main():

    # VARIABLES DE ENTRADA
    circuito: str
    nombre: str
    hi: int  # Hora de inicio
    mi: int # minutos de inicio
    minutos: int #  datos de los tiempos por vuelta
    seg: int
    cseg: int
    segpit: int
    cauchos: int

    # VARIABLES DE PROCESO
    duracion: int # acumulador de la duración en centesimas de segundo de la carrrera
    band: int

    # VARIABLES DE SALIDA
    contadorpit: int # contador de las veces que entró a pit
    mr: int # datos del tiempo de vuelta mas rápido
    sr: int
    csr: int
    hf: int # hora de finalización
    mf: int
    minc: int # datos de la duración de la carrera
    segc: int
    csegc: int

    # apertura de archivo
    arch = open("carrera.txt", "r")

    # lectura de la primera línea del archivo
    registro = arch.readline()
    linea = registro.split(',')
    circuito = linea[0]
    nombre = linea[1]
    hi = int(linea[2])
    mi = int(linea[3])

    # inicialización de contadores y acumuladores
    contadorpit = 0
    duracion = 0
    band = 0

    # inicio de ciclo
    for registro in arch:

        minutos, seg, cseg, segpit, cauchos = leer(registro)

        # determinar si entrá al pit
        if segpit > 0:
            contadorpit = contadorpit + 1

        # cálculo de la duracion de la carrera
        duracion += transformar(minutos, seg, cseg) + (segpit * 1000)

        # cálculo de la vuelta mas rápida
        if band == 0:
            band = 1
            mr = minutos
            sr = seg + segpit
            csr = cseg
        else:
            mr, sr, csr = menor(mr, sr, csr, minutos, seg + segpit, cseg)

    print("Circuito: ", circuito)
    print("Piloto: ", nombre)
    # impresion de la duracion de la carrera
    minc, segc, csegc = devolucion(duracion)
    print("Duración de la carrera:%d min %d seg %d cseg " % (minc, segc, csegc))

    # impresión de la hora de finalización
    hf, mf = sumahora(hi, mi, minc)
    print("Hora de finalizacion de la carrera: %d : %d " % (hf, mf))

    # impresión del tiempo mas rápido
    print("Tiempo mas rápido: %d min %d seg %d cseg " % (mr, sr, csr))

    # impresión del numero de paradas a pit stop
    print("Entradas a pit stop: ", contadorpit)

    arch.close()

    # Mensaje al usuario
    input("Pulse una tecla para finalizar")

if __name__ == "__main__":
    main()
