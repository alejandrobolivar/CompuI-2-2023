'''
La policía de tránsito de ciudad Gótica debido a la gran cantidad de accidentes de tránsito
ocurridos en los últimos meses por exceso de velocidad decide crear cuatro turnos de vigilancia,
teniendo cada turno su propio límite de velocidad. Para controlar la velocidad a la cual circulan
los vehículos se colocan cámaras y sensores de velocidad en varios puntos de los cuadrantes,
así para cada vehículo, al momento de ser monitoreado se toma el registro del vehículo
(número de placa) y la velocidad real a la cual circulaba al momento de ser monitoreado,
en millas por hora, esta información se envía inmediatamente al departamento de tránsito
donde se genera para conductor la siguiente data:
 
Nombre del conductor, Genero (1: Femenino 2: Masculino), Hora de circulación, velocidad registrada (millas/hora)
 
Desarrolle un programa que procese la información anterior
para un grupo de conductores y determine e imprima:

Para cada conductor:
1)Indicar si es infractor o no, en caso de serlo  la multa que debe pagar.

Para todos los conductores:
2)Porcentaje de vehículos que circularon en el turno 2 que no fueron infractores con respecto al total de conductores reportados en ese turno.
3)Cuantos vehículos fueron procesados por el departamento de tránsito después de encontrar el primer infractor del turno 2.
4)Nombre y multa pagada por el  tercer conductor del género masculino.
5)Promedio de las multas canceladas por los conductores del turno 1 del género femenino.

Consideraciones:
Los horarios de los turnos son 1: hasta el mediodía, 2: después del mediodía.
Los límites de velocidad son: 80 km/hora para el turno 1; y 60 km/hora para el turno  2.
La multa a pagar será de 2.50 $ por cada  milla/hora que se excedió la velocidad límite.
Una milla/hora equivale a 1,61 km/hora.
'''

# Inicialización
cont_veh_t2_ni = 0
cont_veh_t2 = 0
band_p3 = 0
cont_p4 = 0
cont_p5 = 0
acum_p5 = 0
resp = 'S'

while resp.upper() == 'S':
    # Lectura de variables de entrada
    conductor = input("Nombre del Conductor:")
    genero = int(input("Genero [Femenino:1, Masculino:2]:"))
    hh_circ = int(input("Hora de Circulacion :"))
    vel_reg = float(input("Velocidad Registrada :"))
    vel_reg2 = vel_reg * 1.61  # Convertir a km/h

    if (hh_circ <= 12 and vel_reg2 <= 80) or (hh_circ > 12 and vel_reg2 <= 60):
        print("No es infractor")
        if hh_circ > 12: # Turno 2
            cont_veh_t2_ni += 1
    else:
        if hh_circ <= 12: # Turno 1
            print("Es infractor del Turno 1")
            multa = 2.5 * (vel_reg - 80 / 1.61)
            if genero == 1:
                acum_p5 += multa
                cont_p5 += 1
        else:  # Turno2
            print("Es infractor del Turno 2")
            cont_veh_t2 += 1
            multa = 2.5 * (vel_reg - 60 / 1.61)
            if band_p3 == 0: # Primer infractor del turno 2
                cant_p3 = 0
                band_p3 = 1
            else:
                cant_p3 += 1
        print("El conductor es infractor y pagará una multa de $" , multa)
        if genero == 2 and cont_p4 < 3:
            cont_p4 += 1
            if cont_p4 == 3:
                conductor_p4 = conductor
                multa_p4 = multa
    resp = input("¿Hay más conductores [S/N]?: ")

if cont_veh_t2 > 0:
    porc_p2 = cont_veh_t2_ni / cont_veh_t2 * 100
    print("2) Porcentaje de vehículos que circularon en el turno 2 que no fueron infractores con respecto al total de conductores reportados en ese turno= " ,  porc_p2, " %")
else:
    print("2) No hubo infractores en el Turno 2")

print("3) Cuantos vehí­culos fueron procesados por el departamento de tránsito después de encontrar el primer infractor del turno 2= " & cant_p3)

if cont_p4 == 3:
    print("4) Nombre y multa pagada por el tercer conductor del género masculino= " , conductor_p4 , " pagó $" , multa_p4)
else:
    print("4) Hubo solamente " , cont_p4 , " conductores masculinos infractores")

if cont_p5 > 0:
    prom_p5 = acum_p5 / cont_p5
    print("5) Promedio de las multas canceladas por los conductores del turno 1 del género femenino= " , prom_p5)
else:
    print("5) No hubo infractoras en el Turno 1")