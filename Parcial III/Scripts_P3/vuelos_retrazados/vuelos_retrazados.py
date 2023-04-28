# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 20:09:08 2022

' Ejercicio de preparaduria. Vuelos retrazados
' Elaborado por: Alejandro Bolívar
' Fecha: 23-04-2022

@author: bolivar

Tiempo de retardo en los vuelos
OBJETIVO: Desarrollar un programa, cuya solución implemente funciones.

Problema:
Para la administración y mejora del funcionamiento de un Aereopuerto
Nacional, se registra a cada vuelo que parte en el día, el número de vuelo, la
hora de salida programada del vuelo y además se registra la hora real, en la
cual se hace efectivo el despege del mismo (Los tiempos estan expresados en
hora militar). De esta manera, es posible calcular el tiempo de demora que un
vuelo tuvo expresado en minutos es decir, la diferencia entre la hora de salida
real y la programada da un valor positivo.
Nota:
1.- Si el avión logra salir antes de la hora programada el tiempo de demora es
cero o negativo.
2.- Considere que todos los vuelos se realizan durante el mismo día.
3.- Recuerde que: 1 Hora = 60 Minutos

PROBLEMA:
En un archivo de datos de nombre ‘vuelos.dat’ se almaceno en cada línea la
siguiente informacion de cada vuelo realizado en un día, el número de vuelo,
la hora de salida programa (expresada en formato militar; hh:mm) y la hora de
salida real (expresada en formato militar; hh:mm). Desarrolle un programa que
determine e imprima hacia el archivo de datos ‘resultados.dat’ el número de vuelo,
la salida programada y el tiempo de demora (expresado en hh: mm), y por
pantalla reporte la informacion de cual fue el vuelo con la mayor demora.

REQUERIMIENTOS:
Para la solución del problema debe definir y utilizar:
1. Defina una estructura tipo registro de nombre “Tiempo”, capaz de almacenar
un tiempo expresado en horas (HH) y nminutos (MM).
2. Defina una estructura tipo registro de nombre “Vuelo”, capaz de almacenar
el numero de vuelo y dos tiempos tipo hora .
3. Un subprograma que lea desde archivo de datos una línea que contenga
la informacion del número de vuelo de un avión, la hora pautada de salida y
la hora en que realmente salio.
4. Un subprograma que convierta un tiempo expresado en horas y minutos y
devuelva el tiempo expresado en minutos.
5. Un subprograma que dado dos tiempos expresados en horas y minutos, devuelva,
¿cuantos minutos han trasncurridos entre ambos?
6. Un subprograma que imprima hacia un archivo de datos (sin salto de línea),
un tiempo expresado en horas y minutos de la siguiente manera, las horas y
los minutos representado en dos digitos y separdos por dos puntos (:), en caso de
ser el valor inferior a 10, imprima un cero por delante

Ejemplo de los archivos:
Por ejemplo:
vuelos.dat
201 6 15 7 20
205 7 00 6 50
301 8 00 8 00
302 9 15 10 40
305 16 20 16 35

resultados.dat
VUELO HORA_SALIDA DEMORA(hh:mm)
201 06:15 01:05
205 07:00 a tiempo
301 08:00 a tiempo
302 09:15 01:25
305 16:20 00:15

Salida por pantalla:
El vuelo con mayor demora fue el 302 con salida programada a las 09:15 con 85
minutos de demora
"""

# Programa que lee una linea del archivo "arch"
def leerpuntos(registro):
    linea = registro.split(',')
    identif = int(linea[0])
    hp = int(linea[1])
    mp = int(linea[2])
    hs = int(linea[3])
    ms = int(linea[4])
    return identif, hp, mp, hs, ms

# Convierte a Minutos
def enmin(h, m):
    return m + h * 60

# Determina el delta t en minutos
def deltat(h1, m1, h2, m2):
    return enmin(h2, m2) - enmin(h1, m1)

# Imprime la hora en formato 00:00 sin saltar de linea
def imprimehora(arch, h, m):
    arch.write('%02d:%02d\t' % (h, m))

def main():
    # datos de vuelo
    identif: int
    hpro: int
    mpro: int
    hsal: int
    msal: int
    # Mayor retrados
    mid: int
    mm: int
    mh: int
    mret: int
    # Variables Auxiliares
    retraso: int
    h: int
    m: int

    # Manejo de Archivos
    arch1 = open("vuelos.txt", "r")
    arch2 = open("resultados.txt", "w")

    mret = 0

    for registro in arch1:
        # lectura de datos
        identif, hpro, mpro, hsal, msal = leerpuntos(registro)

        # impresión
        arch2.write(str(identif) + '\t')
        imprimehora(arch2, hpro, mpro)
        retraso = deltat(hpro, mpro, hsal, msal)

        # Busco el mayor retraso
        if retraso > mret:
            mid = identif
            mh = hpro
            mm = mpro
            mret = retraso

        if retraso <= 0:
            arch2.write("A tiempo")
        else:
            # Desglose en Horas y minutos, se pudo haber construido un sub que lo realice
            h = retraso // 60
            m = retraso % 60
            imprimehora(arch2, h, m)
        arch2.write('\n')

    # Impresion por pantalla
    print("El vuelo con mayor demora fue el %d con salida programada a las %02d:%02d con %d minutos de demora" % (mid, mh, mm, mret))

    # Cierre de archivos
    arch1.close()
    arch2.close()

    # Mensaje al usuario
    input("Pulse una tecla para finalizar")

if __name__ == "__main__":
    main()
