# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 12:07:16 2022

@author: bolivar

Escenario: Los Autos Locos
El Campeonato mundial de autos locos ha decidido que a partir de esta temporada, la
parrilla de partida se establecerá por clasificación. Para ello desean que cada auto,
debe girar un circuito de 50 km el número de veces que deseen en un periodo de 1.5
horas y aquel que realice la trayectoria en el menor tiempo es el que parte de primero.
Para ello un día antes de la carrera registraron en el archivo “Clasificacion.txt”, la
siguiente información ordenada por conductor:
Nombre del Conductor, Hora Inicio y fin del recorrido (HH, MM, SS)
Ejemplo:
    
Pier
09, 03, 15, 09, 15, 59, 0
09, 30, 35, 10, 05, 00, 1
Penélope
08, 10, 00, 08, 20, 12, 0
08, 25, 07, 09, 09, 03, 0
09, 15, 00, 09, 30, 00, 1
El Varón rojo
11, 37, 00, 12, 00, 00, 1

Nota: el tiempo está expresado
en Horas (HH), minutos (MM) y
segundos (SS).

Enunciado
Elabore un programa que dado el archivo “Clasificados.txt”, determine e imprima por pantalla los
siguientes resultados:
Para cada conductor:
• Nombre del Conductor, tiempo menor realizado, Velocidad promedio en la ejecución del recorrido (Km/H).
Para todos los usuarios:
• Nombre del Conductor que realiza el recorrido con el menor tiempo.
• Porcentaje de Conductores que pudieron realizar el recorrido en más de dos veces.
Requerimientos mínimos:
1- Elabore un Subprograma que lea una línea de un archivo de datos que contiene una cadena de 15 caracteres,
dos tiempos expresados en horas, minutos y segundos, y el valor del centinela.
2- Elabore un subprograma que transforme un tiempo expresado en horas, minutos y segundos en su
equivalente en segundos.
3- Elabore un subprograma que transforme dos tiempos expresados en horas, minutos y segundos y determine el
tiempo transcurrido entre ambos.
4- Elabore un subprograma que dado un tiempo en segundos, lo transforme en horas, minutos y segundos.
5- Elabore un subprograma que dado dos tiempos en horas, minutos y segundos, indique con un valor booleano
si el tiempo1 es menor al tiempo2.
6- Elabore un subprograma que imprima por pantalla sin salto de línea, un tiempo expresado en horas, minutos y
segundos con un formato de dos dígitos y separados por dos puntos. Ejemplo: 00:45:05

Salida por pantalla:
pier   Tiempo Transc.:   0:12:44  Velocidad Promedio: 161.38
Penelope   Tiempo Transc.:   0:10:12  Velocidad Promedio: 187.47
El varon rojo   Tiempo Transc.:   0:23:0  Velocidad Promedio: 130.43
Nombre del Conductar más rápido: Penelope
Porcentaje de Conductores que pudieron realizar el recorrido en más de 2 veces= 33.33% 
    
"""
# Escenario: Los Autos Locos

# Procedimiento que permite Leer el nombre del conductor del archivo
def LeeNomb(contenido, linea):
    Nombre = contenido[linea].strip()
    return Nombre


# Procedimiento que lee los valores de hora para cada uno de los campos de la estructura Horas
def leeHora(contenido, linea):
    s = [0,0,0]
    t = [0,0,0]
    linea = contenido[linea].split(',')
    s[0] = int(linea[0])
    s[1] = int(linea[1])
    s[2] = int(linea[2])
    t[0] = int(linea[3])
    t[1] = int(linea[4])
    t[2] = int(linea[5])
    cent = int(linea[6])
    return s, t, cent


# Función que convierte las horas y minutos en segundos
def TiempoSeg(T: list):
    return T[0] * 3600 + T[1] * 60 + T[2]


# Función que calcula en tiempo transcurrido entre dos horas
def TiempoTranscurrido(Hi: list, Hf: list):
    return TiempoSeg(Hf) - TiempoSeg(Hi)


# Función que determina el menor tiempo o mejor tiempo
def TMenor(T: int, TM: int):
    TMen = TM
    if T < TM:
        TMen = T
    
    return TMen


# Función que convierte el tiempo(segundos) a horas. minutos y segundos
def ConvHMS(T: int):
    H = [0,0,0]
    H[0] = (T // 3600)
    H[1] = (T % 3600) // 60
    H[2] = ((T % 3600) % 60)

    return H

# Función que calcula la velocidad
def Velocidad(d: float, T: int):
    return d / (T / 3600)


# Procedimiento que determina el conductor con mejor tiempo de recorrido
def CondMenTime(nombre:str, nombreMen:str, T:int, TMen:int):
    if T < TMen:
        nombreMen = nombre
        TMen = T
    
    return nombreMen, TMen


# Procedimiento que imprime en pantalla
def ImprimePant(nomb, trev: list, Vel: float):
    print(nomb + "   Tiempo Transc.:   " + str(trev[0]) + ":" + str(trev[1]) + ":" + str(trev[2]) + "  Velocidad Promedio: %.2f" % Vel)


def main():
    # Var. Entrada
    C = [str,[0,0,0],[0,0,0],0]
    # Var. Proceso
    cent: int
    TT: int
    TM: int
    T: int
    Cont: int
    ContV: int
    ContC: int
    AcumVel: float
    # Var. Salida
    Trev = [0,0,0]
    Porcmas2: float
    VelPro: float
    CMt: str = ""
    DIST = 50

    arch = open("clasificacion.txt", 'r')
    contenido = arch.readlines()
    linea = 0
    Cont = 0 
    ContC = 0 
    T = 100000
    
    while linea < len(contenido):
        
        C[0] = LeeNomb(contenido, linea)
        linea += 1
        
        cent = 0
        ContC += 1
        ContV = 0
        AcumVel = 0
        TM = 1000000
        
        while cent == 0:
            
            C[1],C[2],cent = leeHora(contenido, linea)
            linea += 1
            
            TT = TiempoTranscurrido(C[1], C[2])
            TM = TMenor(TT, TM)
            ContV += 1
            AcumVel += Velocidad(DIST, TT)

        Trev = ConvHMS(TM)
        VelPro = AcumVel / ContV
        ImprimePant(C[0], Trev, VelPro)
        
        CMt, T = CondMenTime(C[0], CMt, TM, T)
        
        if ContV > 2:
            Cont += 1

    print("Nombre del Conductar más rápido: %s" % CMt)
    
    if Cont > 0:
        Porcmas2 = Cont * 100 / ContC
        print("Porcentaje de Conductores que pudieron realizar el recorrido en más de 2 veces= %.2f" % Porcmas2 + '%')

    # Mensaje al usuario
    input("Pulse una tecla para finalizar")

if __name__ == "__main__":
    main()