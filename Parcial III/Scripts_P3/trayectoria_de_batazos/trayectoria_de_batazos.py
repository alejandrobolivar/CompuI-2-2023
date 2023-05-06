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
en el archivo entrenamiento.txt, ver ejemplo.
NOTA: En todos los campos de beisbol, la distancia entre home y 2da. base es de 36.88 m, en cambio la distancia del home al
muro depende del estadio y se encuentra entre 115.82 m a 137.16 m.

Programa Principal
Elabore un programa que dado el archivo de datos entrenamiento.txt, determine e imprima por pantalla:
Para cada batazo:
nro. Batazo, velocidad de salida (m/s), distancia horizontal máxima de alcance (m), altura del batazo (m) y situación del batazo*
*Situación del batazo es:
0 = Está dentro del cuadro (distancia <= 36.88)
1 = Cae en los outfielders (36.88 < distancia <= largo del campo) O ((distancia > largo del campo) Y (la altura del batazo es inferior a la del muro))
2 = Jonrón, la sacó del parque (distancia > largo del campo) Y (la altura del batazo es superior a la del muro)
Para todos los batazos, velocidad y ángulo de salida del jonrón más largo dado por un bateador.

Requerimientos
Construya e implemente los siguientes subprogramas:
1. (2 puntos) Un subprograma que dado un ángulo en grados determine su valor en radianes.
2. (3 puntos) Un subprograma que dada la distancia del home al muro (x), altura del bateo (y0), la velocidad (v0) y ángulo
(alfa) de salida del batazo, devuelva la altura del batazo. Dónde:
    altura_batazo = y0 + x * math.tan(alfa) - (g * x ** 2) / (2 * v0 ** 2 * math.cos(alfa) ** 2)
3. (3 puntos) Un subprograma que dada la velocidad (v0) y ángulo (alfa) de salida del batazo,
devuelva la distancia horizontal máxima de alcance y situación del batazo (según se
especifica en el enunciado). Dónde:
    xmax = v0 ** 2 * math.sin(2 * alfa) / g
    
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
nro Velsalida xmax Y Situación
1 24,2 13,43 -9984,50 0
2 35,29 78,86 -244,45 1
3 37 131,98 2,81 1
4 37,1 139,01 9,89 2

Recuerde
1 π (radianes) = 180º; g=9.81 m/s2
Funciones trigonométricas requeridas: math.sin(x) : math.cos(x) : math.tan(x) ‘Donde x es el ángulo expresado en radianes
"""

import math

def Convertir_Radianes(grados: float):
    return grados * math.pi / 180

def altura_batazo(x:float, y0: float, v0: float, alfa: float):
    g = 9.81 # m/s
    altura_batazo = y0 + x * math.tan(alfa) - (g * x ** 2) / (2 * v0 ** 2 * math.cos(alfa) ** 2)
    return altura_batazo

def calculos(v0: float, alfa: float, largo_campo: float, altura_muro: float, y0: float):
    g = 9.81 # m/s
    Y: float
    xmax = v0 ** 2 * math.sin(2 * alfa) / g
    y = altura_batazo(largo_campo, y0, v0, alfa)
    if xmax <= 36.88:
        situacion = 0
    elif xmax > largo_campo and Y > altura_muro:
        situacion = 2
    else:
        situacion = 1

    return xmax, situacion

def leer(registro):
    linea = registro.split(',')
    altura_bateo = float(linea[0])
    velocidad_salida = float(linea[1])
    angulo_salida = float(linea[2])
    return altura_bateo, velocidad_salida, angulo_salida

def main():

    # Variables a leer del Archivo
    largo_campo: float # m
    altura_muro: float # m
    altura_bateo: float # m
    velocidad_salida: float # m/s
    angulo_salida: float # Grados

    # Resultados a mostrar al Usuario por consola
    xmax: float # Distancia Horizontal Máxima de alcance (m)
    Y: float # Altura del Batazo (m)
    situacion: int # 0=Dentro del Cuadro, 1=Outfielders, 2=Jonron
    mvelocidad: float # Velocidad de Salida del Jonron con mayor distancia Horizontal máxima
    mangulo: float # Angulo de Salida del Jonron con mayor distancia Horizontal máxima

    # Variables de Proceso
    angulo_radianes: float # Angulo de Salida expresado en radianes
    Mayor: float # Mayor Distancia Horizontal Máxima}
    bandera: int # bandera del Mayor
    nro: int # Contador de Batazos

    # Apertura y Modo de uso de Archivos
    arch = open("entrenamiento.txt", 'r')

    # Inicialización de Variables
    bandera = 0
    nro = 0

    # Lectura de datos del Campo de Juego

    contenido = arch.readline()
    datos = contenido.split(',')
    largo_campo = float(datos[0])
    altura_muro = float(datos[1])

    # Lectura y proceso de cada Batazo
    # inicio de ciclo
    for registro in arch:

        altura_bateo, velocidad_salida, angulo_salida =  leer(registro)

        # Calculos por cada Batazo
        nro = nro + 1
        angulo_radianes = convertir_radianes(angulo_salida)
        Y = altura_batazo(largo_campo, altura_bateo, velocidad_salida, angulo_radianes)
        xmax, situacion = calculos(velocidad_salida, angulo_radianes, largo_campo, altura_muro, altura_bateo)
        # Impresión de resultados por cada Batazo
        print('%d %.2f %.2f %.2f %d' % (nro, velocidad_salida, xmax, y, situacion))

        # Calculos para todos los Batazos
        if situacion == 2: # Es un jonron
            if bandera == 0: # Es el primer jonron
                mayor = xmax
                mvelocidad = velocidad_salida
                mangulo = angulo_salida
                bandera = 1
            elif xmax > mayor:
                mayor = xmax
                mvelocidad = velocidad_salida
                mangulo = angulo_salida

    # Impresión de Resultados para todos los Batazos
    if bandera == 0:
        print("No hubo Jonrones")
    else:
        print("Jonron más Largo:")
        print("Velocidad= %.2f" % mvelocidad)
        print("Angulo= %.2f°" % mangulo)

    # Mensaje al usuario
    input("Pulse una tecla para finalizar")

if __name__ == "__main__":
    main()
