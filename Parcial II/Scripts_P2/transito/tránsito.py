# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 11:48:03 2022

@author: bolivar
"""
'''
La policía de tránsito de ciudad Gótica, debido a la gran cantidad
de accidentes de tránsito ocurridos en los últimos
meses por exceso de velocidad, decide dividir la
ciudad en cuatro cuadrantes, teniendo cada
cuadrante su propio límite de velocidad. Para
monitorear la velocidad a la cual circulan los
vehículos se colocan cámaras y sensores de
velocidad en varios puntos de los cuadrantes. De
cada vehículo se registra la placa y la velocidad
que llevaba al ser monitoreado, en millas por
hora. Esta información se envía inmediatamente
al departamento de tránsito donde se genera para cada vehículo lo siguiente:
Placa del vehículo, Cuadrante por el cual circulaba (1, 2, 3 ó 4) y velocidad registrada (millas/hora)
Desarrolle una aplicación de consola VB2010 que procese la información anterior para un grupo de
vehículos y determine e imprima:
Para cada vehículo:
1. Indicar si es infractor o no, en caso de serlo, la multa en $ que debe pagar. (4 puntos)
Para todos los vehículos:
2. Porcentaje de vehículos que circularon por el cuadrante 4 que no fueron infractores con
respecto al total de vehículos reportados en ese cuadrante. (3 puntos)
3. Cuantos vehículos fueron procesados por el departamento de tránsito antes de encontrar al
primer infractor. (2 puntos)
4. Promedio de dólares cancelados por concepto de multas. ( 2 puntos)
Consideraciones:
a) Los límites de velocidad son:
 80 km/hora para los cuadrantes 1 y 2
 60 km/hora para los cuadrantes 3 y 4
b) La multa a pagar será de 2.50 $ por cada milla/hora que se
excedió la velocidad límite.
c) Una milla/hora equivale a 1,61 km/hora.
Definiciones:
Infractor: El que comete una infracción
Infracción: Incumplimiento de algún tipo de norma que regula un comportamiento en un contexto determinado.
'''

# Variables de Entrada
conductor: str = ""
genero: int
hh_circ: int
vel_reg: float

# Variables de proceso
cont_veh_t2_ni: int
cont_veh_t2: int
band_p3: int
cont_p4: int
cont_p5: int
acum_p5: float
vel_reg2: float

# Variables de Salida
multa: float
porc_p2: float
cant_p3: int
conductor_p4: str = ""
multa_p4: float
prom_p5: float

# inicializacion de variables
cont_veh_t2_ni = 0
cont_veh_t2 = 0
band_p3 = 0
cont_p4 = 0
cont_p5 = 0
acum_p5 = 0

# Manejo de archivos
with open("datostransito.txt", 'r') as arch1, open("resultados.txt", 'w') as arch2:

    # Proceso
    for registro in arch1:
        # lectura de datos
        contenido = registro.split(',')
        nombre = contenido[0]
        genero = int(contenido[1])
        hh_circ = int(contenido[2])
        vel_reg = float(contenido[3])
        vel_reg2 = vel_reg * 1.61  # Convertir a km/h
        if (hh_circ <= 12 and vel_reg2 <= 80) or (hh_circ > 12 and vel_reg2 <= 60):
            arch2.write(f"{nombre} No es infractor\n")
            if hh_circ > 12:  # Turno 2
                cont_veh_t2_ni += 1
        else:
            if hh_circ <= 12: # Turno 1
                arch2.write(f"{nombre} es infractor del Turno 1")
                multa = 2.5 * (vel_reg - 80 / 1.61)
                if genero == 1:
                    acum_p5 += multa
                    cont_p5 += 1
            else: # Turno2
                arch2.write(f"{nombre} es  infractor del Turno 2")
                cont_veh_t2 += 1
                multa = 2.5 * (vel_reg - 60 / 1.61)
                if band_p3 == 0: # Primer infractor del turno 2
                    cant_p3 = 0
                    band_p3 = 1
                else:
                    cant_p3 += 1
            arch2.write(f" y pagará una multa de ${multa:.2f}\n")
            if genero == 2 and cont_p4 < 3:
                cont_p4 += 1
                if cont_p4 == 3:
                    conductor_p4 = nombre
                    multa_p4 = multa
    if cont_veh_t2 > 0:
        porc_p2 = cont_veh_t2_ni / cont_veh_t2 * 100
        print("2) Porcentaje de vehículos que circularon en el turno 2 que no fueron infractores con respecto al total de conductores reportados en ese turno= %.2f %%" % porc_p2)
    else:
        print("2) No hubo infractores en el Turno 2")
    print(f"3) Cuantos vehículos fueron procesados por el departamento de tránsito después de encontrar el primer infractor del turno 2= {cant_p3}")
    if cont_p4 == 3:
        print(f"4) Nombre y multa pagada por el tercer conductor del género masculino= {conductor_p4} pagó $ {multa_p4:.2f}")
    else:
        print(f"4) Hubo solamente {cont_p4} conductores masculinos infractores")
    if cont_p5 > 0:
        prom_p5 = acum_p5 / cont_p5
        print("5) Promedio de las multas canceladas por los conductores del turno 1 del género femenino= %.2f" % prom_p5)
    else:
        print("5) No hubo infractoras en el Turno 1")