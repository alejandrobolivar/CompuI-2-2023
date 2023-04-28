# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 08:19:29 2022

@author: bolivar

Estadísticas hacia el Mundial

Requerimientos
a) Desarrolle un subprograma que lea de un archivo dos valores tipo integer (El número del archivo pasa
como parámetro)
b) Desarrolle un subprograma que dados dos valores A y B tipo integer, devuelva
1 sí A<B ; 2 sí A=B ; 3 sí A>B
c) Desarrolle un subprograma que dados Partidos Ganados, Partidos Empatados y Diferencia de
Goles determine Puntaje Real y Puntaje Virtual usando las siguientes fórmulas:
Puntaje Real = Partidos Ganados*3 + Partidos Empatados
Puntaje virtual = Puntaje Real + Diferencia de Goles
d) Desarrolle un subprograma dados un valor string y tres valores integer, los escriba como una línea
de un archivo (El número del archivo pasa como parámetro)

Programa Principal
En el archivo “estadísticas.txt”, se registró para cada país que participará en el mundial 2026
los resultados obtenidos durante los últimos N partidos, con la finalidad de poder establecer
predicciones de su posible actuación en el mundial 2026. En el archivo de datos se tiene una
primera línea con el Número de países y el Número N de partidos registrados para cada país y en las
siguientes líneas por cada país se registró el nombre del país y los resultados de cada uno de los N
partidos, como se indica a continuación:
Nombre del País, GFpartido1, GCpartido1, GFpartido2, GCpartido2, … GFpartidoN, GCpartidoN
Donde: GF=Goles a Favor y GC=Goles en contra

Ejemplo del posible archivo “estadísticas.txt”
5 , 3
Italia ,1 ,1 ,1 ,1 ,2 ,0
España ,1 ,1 ,5 ,0 ,2 ,0
Portugal ,0 ,1 ,3 ,2 ,2 ,1
Francia ,1 ,1 ,2 ,0 ,0 ,2
Alemania ,2 ,0 ,2 ,1 ,2 ,1

Desarrolle un programa que usando apropiadamente los subprogramas desarrollados, lea la información del archivo
“estadísticas.txt”, y determine e imprima a un archivo de nombre “pronostico.txt”, por cada país: nombre, diferencia de goles,
puntaje real y puntaje virtual. Adicionalmente debe imprimir por pantalla, el país con más probabilidad de participar en la final
del mundial Brasil 2014, es decir, el que tenga mayor puntaje virtual.

Notas
Se conoce el número de países en el archivo y el número de partidos de cada país. Todos los países tienen el mismo número de partidos
Goles a Favor son los anotados por el equipo
Goles en contra son los que le anotan al equipo
Partido Ganado es aquel en el que GF>GC ; Partido Empatado es aquel en el que GF=GC

Ejemplo de la salida:
pronostico,txt
Pais   Dif.Goles   Puntaje Real   Puntaje Virtual
Italia  2 5 7
España  7 7 14
Portugal  1 6 7
Francia  0 4 4
Alemania  4 9 13

Salida por pantalla:
Cantidad de partidos jugados: 3
Pais mas probable: España 

"""

def leer_partido(lista, i, j):
    gf = int(lista[i])
    gc = int(lista[j])
    return gf, gc

def resultado(a, b):
    if a < b:
        resultado = 1
    elif a == b:
        resultado = 2
    else:
        resultado = 3
    return resultado


# Subprograma que determina la diferencia de dos valores
def diferencia(a: int, b: int):
    return a - b


# Subprograma que determina el Puntaje Virtual de un pais
def puntaje(pg, pe, dg):
    puntaje_real = pg * 3 + pe
    puntaje_virtual = puntaje_real + dg
    return puntaje_real, puntaje_virtual


# Subprograma que lee la informacion de un pais contenido en una linea del archivo
# de lectura "Apartidos.txt", que se encuntra definido como el Nro 1
def LeerPais(registro):
    # Subprograma que lee la informacion de una linea del archivo
    linea = registro.split(',')
    nom = linea[0]
    pg = 0
    pe = 0
    pp = 0
    dg = 0
    i = 1
    while i < len(linea):
        gf, gc = leer_partido(linea, i, i+1)
        i += 2
        if resultado(gf, gc) == 3:
            pg += 1
        elif resultado(gf, gc) == 2:
            pe += 1
        else:
            pp += 1

        dg += diferencia(gf, gc)
    return nom, pg, pe, pp, dg


# Subprograma que Imprime el nombre de un pais, diferencia de goles, puntaje real y virtual al
# archivo de salida "Pronostico.txt", que se encuentra definido como el Nro 2
def ImprimirPronostico(arch, nombre, dg, pr, pv):
    arch.write("%s %d %d %d\n" % (nombre, dg, pr, pv))


def main():

    # Que Quiero
    pais_probable: str

    # Variables Auxiliares
    Primero: bool = True

    # Manejo de Archivos
    arch1 = open("partidos.txt", "r")
    arch2 = open("pronosticos.txt", "w")

    contenido = arch1.readlines()
    cp = int(contenido[0])  # cantidad de partidos
    linea = 1  # Posición del siguiente elemento
    
    # Impresion de un titulo al archivo de salida
    arch2.write("Pais   Dif.Goles   Puntaje Real   Puntaje Virtual\n")

    # Ciclo de lectura
    for i in range(1,len(contenido)):  # CICLO QUE PROCESA los países
        
        nom, pg, pe, pp, dg = LeerPais(contenido[linea])
        linea += 1
        pr, pv = puntaje(pg, pe, dg)

        # Impresion del pronostico del pais o equipo
        ImprimirPronostico(arch2, nom, dg, pr, pv)

        # Determinacion del equipo con mas probabilidad
        if Primero:
            Primero = False
            pais_probable = nom
            pvmax = pv
        elif pv  > pvmax :
            pais_probable = nom
            pvmax = pv

    # Cierre de archivos
    arch1.close()
    arch2.close()

    # Impresion por pantalla del pais mas probable
    print("Cantidad de partidos jugados: %d" % cp)
    print("Pais mas probable: %s" % pais_probable)
    
    # Mensaje al usuario
    input("Pulse una tecla para finalizar")

if __name__ == "__main__":
    main()
