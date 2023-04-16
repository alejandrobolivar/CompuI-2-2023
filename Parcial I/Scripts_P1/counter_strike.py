'''
Counter Strike es un juego de acción en primera persona, de tipo
multijugador, que puede ser jugado en red tipo LAN (Local Área
Network) u Online.
En la actualidad y en virtud de la fama de este juego, el
Departamento de Computación de la Facultad de Ingeniería ha
programado un campeonato de Counter Strike. Con el objetivo
de medir fuerzas entre profesores y estudiantes, se le pide a usted
que, considerando la siguiente información de los L participantes
inscritos:

NOMBRE DEL JUGADOR, EQUIPO, CANTIDAD DE ENEMIGOS ELIMINADOS Y
CANTIDAD DE VECES QUE FUE ELIMINADO EL JUGADOR

Desarrolle el Algoritmo de un programa que procese esa información y determine:
1)Promedio de enemigos eliminados por el equipo de Estudiantes
2)Nombre del 1er jugador en eliminar a más de 100 enemigos y el equipo al que pertenece
3)Cantidad total de veces que fueron eliminados los jugadores del equipo de Profesores

Consideraciones:
o El Equipo será: 1 = Profesores, 2 = Estudiantes

'Variables de Entrada
L
nombre_j  = ""
equipo
cant_enemigos_elimin, cant_veces_eliminado

'Variables de Proceso
sum_enemigos_elim
cant_est
band_nomb1

'Variables de Salida
prom
nomb1  = ""
equipo1  = ""
cont_total_elim_prof
'''

sum_enemigos_elim = 0
cont_total_elim_prof = 0

L = int(input("Cantidad de Participantes:"))

for _ in range(L):
    # Entrada de datos
    nombre_j = input("Nombre del jugador:")
    equipo = input("Equipo:")
    cant_enemigos_elimin = input("Cantidad de enemigos eliminados:")
    cant_veces_eliminado = input("Cantidad de veces que fue eliminado:")

    # Proceso
    if equipo == 2:  # Equipo de estudiantes
        sum_enemigos_elim +=  cant_enemigos_elimin  # Pregunta 1
        cant_est = cant_est + 1  # Pregunta 2
    else:  # Equipo de profesores
        cont_total_elim_prof +=  cant_veces_eliminado  # Pregunta 3

    if cant_enemigos_elimin >= 100 and band_nomb1 == 0:  # Pregunta 2
        nomb1 = nombre_j
        equipo1 = equipo
        band_nomb1 = 1

# Salida de datos

if cant_est > 0:  # Pregunta 1. Promedio de enemigos eliminados por el equipo de Estudiantes
    prom = sum_enemigos_elim / cant_est
    print("Promedio de enemigos eliminados por el equipo de Estudiantes= " ,prom)
else:
    print("Sin estudiantes")


if band_nomb1 == 1:  # Pregunta 2. Nombre del 1er jugador en eliminar a má¡s de 100 enemigos y el equipo al que pertenece
    print("El jugador " , nomb1 , " fue el 1er jugador en eliminar a más de 100 enemigos")
    print("y el equipo al que pertenece es " , equipo1)
else:
    print("Ningún jugador super los 100 eliminados")


# Pregunta 3. Cantidad total de veces que fueron eliminados los jugadores del equipo de Profesores
print("Cantidad total de veces que fueron eliminados los jugadores del equipo de Profesores= " , cont_total_elim_prof)