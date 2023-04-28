# -*- coding: utf-8 -*-
"""
Created on Wed May 25 17:27:06 2022

@author: bolivar

' Problema: Pregunta 1 parcial Semestre 2-2011
' Escenario: Ensambadora UC Cars
' Solución: 1.1 (Empleando Variables simples)
' Elaborado por: Prof. Hugo Hernández
' Fecha: 08/05/2012
"""

from math import sin, pi
def ConvertirRad(AnguloG):
    ConvertirRad = AnguloG * pi / 180
    return ConvertirRad

def Trabajo(Masa, Distancia, AnguloG):
    # el ángulo en grados
    AnguloR = ConvertirRad(AnguloG)
    trab = Masa * 9.8 * Distancia * sin(AnguloR)
    return trab

def ResultadosPrueba(Masa, Distancia, AnguloG, CReal):
    # el ángulo en grados
    CTeorico = Trabajo(Masa, Distancia, AnguloG) / 3200
    Eficiencia = CTeorico / CReal * 100
    return CTeorico, Eficiencia

'''
def leer_prueba(registro):
    linea = registro.split(',')
    AnguloG = int(linea[0])
    Distancia = int(linea[1])
    CReal = int(linea[2])
    return AnguloG, Distancia, CReal
'''

def ImprimirResultados(arch, AnguloR, Distancia, CReal, CTeorico, Eficiencia, Trab):
    # Subprograma que imprime los Resultados Obtenidos en una prueba
    # hacia un archivo de datos
    arch.write("%.2f, %.2f, %.2f, %.2f, %.2f, %.2f\n" % (AnguloR, Distancia, CReal, CTeorico, Trab, Eficiencia))

def main():
    # Definicion de variables
    # Entrada
    Modelo: str
    Masa: float
    EficMin: float
    Npruebas: int
    Alfa: float
    Creal: float
    Dist: float
    # Salida
    Cteo: float
    Trab: float
    Efic: float
    # Auxiliares
    prom: float
    Acum: float = 0

    # Apertura de archivos
    arch1 = open("pruebas.txt", 'r')
    arch2 = open("resultados.txt", 'w')

    # Lectura de la informacion del auto, También se pudo haber modulado
    
    contenido = arch1.readlines()
    datos = contenido[0].split(',')
    Modelo = datos[0]
    Masa = float(datos[1])
    EficMin = float(datos[2])
    Npruebas = int(datos[3])

    # Ciclo de lectura
    for registro in range(1, Npruebas+1):
        
        datos = contenido[registro].split(',')
        Alfa = float(datos[0])
        Dist = float(datos[1])
        Creal = float(datos[2])

        # Calculos requeridos
        Trab = Trabajo(Masa, Dist, Alfa)
        Cteo, Efic = ResultadosPrueba(Masa, Dist, Alfa, Creal)
        Acum += Efic

        # Impresion de resultados
        ImprimirResultados(arch2, Alfa, Dist, Creal, Cteo, Efic, Trab)

    # Calculo del promedio
    prom = Acum / Npruebas
    arch2.write("Promedio de la Eficiencia = %.2f\n" % prom)

    # Impresion de la situacion del auto
    if prom > EficMin:
        arch2.write("El auto ha pasado las pruebas")
    else:
        arch2.write("El auto no pasó las pruebas")

    # Cierre de archivos
    arch1.close()
    arch2.close()

    # Mensaje al usuario
    print("El programa ha finalizado con exito\n")
    input("Pulse una tecla para finalizar")
    
if __name__ == "__main__":
    main()
