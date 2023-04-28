# -*- coding: utf-8 -*-
"""
Created on Mon May 30 08:23:50 2022

@author: bolivar

Trayectoria de Batazos
Calificación:
Su profesor de física le propuso un tema de investigación de campo que consiste
en estudiar y simular las trayectorias de los batazos de los jugadores de beisbol.
La idea fundamental es crear un programa que dada la siguiente información del
terreno de juego: Distancia del home al muro por el Center Field (m) y Altura del
muro (m), para posteriormente leer la información de los bateos realizados por
un equipo de beisbol en sus prácticas de entrenamiento, donde de cada uno de
ellos se toma: Altura del bateo (m), Velocidad de salida de la pelota (m/s) y
Ángulo de salida (expresado en grados). Almacenándose toda esta información
en el archivo “entrenamiento.txt”, ver ejemplo.
NOTA: En todos los campos de beisbol, la distancia entre home y 2da. base es de 36.88 m, en cambio la distancia del home al
muro depende del estadio y se encuentra entre 115.82 m a 137.16 m.

Programa Principal (3 puntos)
Elabore una aplicación en VB2010 que dado el archivo de datos “entrenamiento.txt”, determine e imprima por pantalla:
Para cada batazo:
Nro. Batazo, velocidad de salida (m/s), distancia horizontal máxima de alcance (m), altura del batazo (m) y situación del batazo*
*Situación del batazo es:
0 = Está dentro del cuadro (distancia <= 36.88)
1 = Cae en los outfielders (36.88 < distancia <= largo del campo) O ((distancia > largo del campo) Y (la altura del batazo es inferior a la del muro))
2 = Jonrón, la sacó del parque (distancia > largo del campo) Y (la altura del batazo es superior a la del muro)
Para todos los batazos, velocidad y ángulo de salida del jonrón más largo dado por un bateador.

Requerimientos (8 puntos)
Construya e implemente los siguientes subprogramas:
1. (2 puntos) Un subprograma que dado un ángulo en grados determine su valor en radianes.
2. (3 puntos) Un subprograma que dada la distancia del home al muro (x), altura del bateo (y0), la velocidad (V0) y ángulo
(α) de salida del batazo, devuelva la altura del batazo. Dónde:
    Altura_Batazo = Y0 + X * Math.Tan(Alfa) - (g * X ** 2) / (2 * V0 ** 2 * Math.Cos(Alfa) ** 2)
3. (3 puntos) Un subprograma que dada la velocidad (V0) y ángulo (α) de salida del batazo,
devuelva la distancia horizontal máxima de alcance y situación del batazo (según se
especifica en el enunciado). Dónde:
    Xmax = V0 ^ 2 * Math.Sin(2 * Alfa) / g
    
Ejemplo de entrada - salida a realizar:

Entrenamiento.txt 
130.5, 3.5
0.54, 24.2, 83.5
0.98, 35.29, 70.8
0.87, 36.7, 53
0.73, 37.1, 48.9

Jonrón más largo:
Velocidad: 37,1
Ángulo: 48,9º

Pantalla
Nro Velsalida Xmax Y Situación
1 24,2 13,43 -9984,50 0
2 35,29 78,86 -244,45 1
3 37 131,98 2,81 1
4 37,1 139,01 9,89 2

Recuerde
1 π (radianes) = 180º; g=9.81m/s2
Funciones trigonométricas requeridas: Math.sin(x) : Math.cos(x) : Math.tan(x) ‘Donde x es el ángulo expresado en radianes
"""

import math

def Convertir_Radianes(Grados: float):
    return Grados * math.pi / 180

def Altura_Batazo(X:float, Y0: float, V0: float, Alfa: float):
    g = 9.81 # m/s
    Altura_Batazo = Y0 + X * math.tan(Alfa) - (g * X ** 2) / (2 * V0 ** 2 * math.cos(Alfa) ** 2)
    return Altura_Batazo

def Calculos(V0: float, Alfa: float, Largo_Campo: float, Altura_Muro: float, Y0: float):
    g = 9.81 # m/s
    Y: float
    Xmax = V0 ** 2 * math.sin(2 * Alfa) / g
    Y = Altura_Batazo(Largo_Campo, Y0, V0, Alfa)
    if Xmax <= 36.88:
        Situacion = 0
    elif Xmax > Largo_Campo and Y > Altura_Muro:
        Situacion = 2
    else:
        Situacion = 1

    return Xmax, Situacion

def leer(registro):
    linea = registro.split(',')
    Altura_Bateo = float(linea[0])
    Velocidad_Salida = float(linea[1])
    Angulo_Salida = float(linea[2])
    return Altura_Bateo, Velocidad_Salida, Angulo_Salida

def main():

    # Variables a leer del Archivo
    Largo_Campo: float # m
    Altura_Muro: float # m
    Altura_Bateo: float # m
    Velocidad_Salida: float # m/s
    Angulo_Salida: float # Grados

    # Resultados a mostrar al Usuario por consola
    Xmax: float # Distancia Horizontal Máxima de alcance (m)
    Y: float # Altura del Batazo (m)
    Situacion: int # 0=Dentro del Cuadro, 1=Outfielders, 2=Jonron
    MVelocidad: float # Velocidad de Salida del Jonron con mayor distancia Horizontal máxima
    MAngulo: float # Angulo de Salida del Jonron con mayor distancia Horizontal máxima

    # Variables de Proceso
    Angulo_Radianes: float # Angulo de Salida expresado en radianes
    Mayor: float # Mayor Distancia Horizontal Máxima}
    Bandera: int # Bandera del Mayor
    Nro: int # Contador de Batazos

    # Apertura y Modo de uso de Archivos
    arch = open("entrenamiento.txt", 'r')

    # Inicialización de Variables
    Bandera = 0
    Nro = 0

    # Lectura de datos del Campo de Juego

    contenido = arch.readline()
    datos = contenido.split(',')
    Largo_Campo = float(datos[0])
    Altura_Muro = float(datos[1])

    # Lectura y proceso de cada Batazo
    # inicio de ciclo
    for registro in arch:

        Altura_Bateo, Velocidad_Salida, Angulo_Salida =  leer(registro)

        # Calculos por cada Batazo
        Nro = Nro + 1
        Angulo_Radianes = Convertir_Radianes(Angulo_Salida)
        Y = Altura_Batazo(Largo_Campo, Altura_Bateo, Velocidad_Salida, Angulo_Radianes)
        Xmax, Situacion = Calculos(Velocidad_Salida, Angulo_Radianes, Largo_Campo, Altura_Muro, Altura_Bateo)
        # Impresión de resultados por cada Batazo
        print('%d %.2f %.2f %.2f %d' % (Nro, Velocidad_Salida, Xmax, Y, Situacion))

        # Calculos para todos los Batazos
        if Situacion == 2: # Es un jonron
            if Bandera == 0: # Es el primer jonron
                Mayor = Xmax
                MVelocidad = Velocidad_Salida
                MAngulo = Angulo_Salida
                Bandera = 1
            elif Xmax > Mayor:
                Mayor = Xmax
                MVelocidad = Velocidad_Salida
                MAngulo = Angulo_Salida

    # Impresión de Resultados para todos los Batazos
    if Bandera == 0:
        print("No hubo Jonrones")
    else:
        print("Jonron más Largo:")
        print("Velocidad= %.2f" % MVelocidad)
        print("Angulo= %.2f°" % MAngulo)

    # Mensaje al usuario
    input("Pulse una tecla para finalizar")

if __name__ == "__main__":
    main()
