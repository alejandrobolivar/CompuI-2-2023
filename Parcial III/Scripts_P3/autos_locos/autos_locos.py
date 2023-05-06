# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 12:07:16 2022

@author: bolivar

Escenario: Los Autos Locos
El Campeonato mundial de autos locos ha decidido que a partir de esta temporada, la
parrilla de partida se establecerá por clasificación. Para ello desean que cada auto,
debe girar un circuito de 50 km el número de veces que deseen en un periodo de 1.5
horas y aquel que realice la trayectoria en el menor tiempo es el que parte de primero.
Para ello un día antes de la carrera registraron en el archivo Clasificacion.txt, la
siguiente información ordenada por conductor:
Nombre del Conductor, Hora Inicio y fin del recorrido en (hh, mm, ss)
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

Nota: el tiempo está expresado en Horas (hh), minutos (mm) y segundos (ss).

Enunciado:
Elabore un programa que dado el archivo Clasificados.txt, determine e imprima por pantalla los
siguientes resultados:
Para cada conductor:
• Nombre del Conductor, tiempo menor realizado, Velocidad promedio en la ejecución del recorrido (km/h).
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
pier   Tiempo Transc.:   00:12:44  Velocidad Promedio: 161.38
Penelope   Tiempo Transc.:   00:10:12  Velocidad Promedio: 187.47
El varon rojo   Tiempo Transc.:   00:23:00  Velocidad Promedio: 130.43
Nombre del Conductar más rápido: Penelope
Porcentaje de Conductores que pudieron realizar el recorrido en más de 2 veces= 33.33%

"""

# Procedimiento que permite Leer el nombre del conductor del archivo
def lee_nomb(contenido, linea):
    return contenido[linea].strip()


# Procedimiento que lee los valores de hora para cada uno de los campos de la estructura Horas
def lee_hora(contenido, linea):
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
def tiempo_seg(t: list):
    return t[0] * 3600 + t[1] * 60 + t[2]


# Función que calcula en tiempo transcurrido entre dos horas
def tiempo_transcurrido(hi: list, hf: list):
    return tiempo_seg(hf) - tiempo_seg(hi)


# Función que determina el menor tiempo o mejor tiempo
def t_menor(t: int, tm: int):
    tmen = tm
    if t < tmen:
        tmen = t
    return tmen


# Función que convierte el tiempo(segundos) a horas. minutos y segundos
def conv_hms(t: int):
    h = [0, 0, 0]
    h[0] = (t // 3600)
    h[1] = (t % 3600) // 60
    h[2] = ((t % 3600) % 60)
    return h


# Función que calcula la velocidad
def velocidad(d: float, t: int):
    return d / (t / 3600)


# Procedimiento que determina el conductor con mejor tiempo de recorrido
def cond_men_time(nombre:str, nombremen:str, t:int, tmen:int):
    if t < tmen:
        nombremen = nombre
        tmen = t

    return nombremen, tmen


# Procedimiento que imprime en pantalla
def imprime_pant(nomb, t_rev: list, vel: float):
    print(
        f"{nomb}   Tiempo Transc.:   {t_rev[0]:02}:{t_rev[1]:02}:{t_rev[2]:02}"
        + "  Velocidad Promedio: %.2f" % vel
    )


def main():
    # Var. Entrada
    c = [str,[0,0,0],[0,0,0],0]
    # Var. Proceso
    cent: int
    tt: int
    tm: int
    t: int
    cont: int
    cont_v: int
    contc: int
    acum_vel: float
    # Var. Salida
    t_rev = [0,0,0]
    porc_mas_2: float
    vel_pro: float
    cmt: str = ""
    DIST = 50

    arch = open("clasificacion.txt", 'r')
    contenido = arch.readlines()
    linea = 0
    cont = 0
    contc = 0
    t = 100000

    while linea < len(contenido):
        c[0] = lee_nomb(contenido, linea)
        linea += 1
        cent = 0
        contc += 1
        cont_v = 0
        acum_vel = 0
        tm = 1000000

        while cent == 0:

            c[1], c[2], cent = lee_hora(contenido, linea)
            linea += 1

            tt = tiempo_transcurrido(c[1], c[2])
            tm = t_menor(tt, tm)
            cont_v += 1
            acum_vel += velocidad(DIST, tt)

        t_rev = conv_hms(tm)
        vel_pro = acum_vel / cont_v
        imprime_pant(c[0], t_rev, vel_pro)

        cmt, t = cond_men_time(c[0], cmt, tm, t)

        if cont_v > 2:
            cont += 1

    print(f"Nombre del Conductar más rápido: {cmt}")

    if cont > 0:
        porc_mas_2 = cont * 100 / contc
        print("Porcentaje de Conductores que pudieron realizar el recorrido en más de 2 veces= %.2f" % porc_mas_2 + '%')

    # Mensaje al usuario
    input("Pulse una tecla para finalizar")

if __name__ == "__main__":
    main()