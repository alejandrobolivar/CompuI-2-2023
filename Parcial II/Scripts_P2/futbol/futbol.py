'''
La FIFA está analizando las estadísticas del mundial, por lo que se almacenó en
 un archivo
de nombre juegos.dat para cada uno de los Partidos, la siguiente información
Fecha del partido, Equipo1, Equipo2, Goles del equipo1, Goles del equipo2
Desarrolle un programa en VB2008, que lea la información y genere dos archivos
 de nombre ganadores.dat y perdedores.dat que deben contener a los equipos
 ganadores, los perdedores respectivamente. La información a escribir en ambos
 archivos es:
    Nombre del equipo y número de goles anotados. Adicionalmente imprima por
    pantalla, la siguiente información:
1. Porcentaje de partidos que quedaron empatados
2. Equipos participantes en el partido donde hubo la mayor cantidad de goles
anotados
Consideraciones
 La fecha del partido se encuentra almacenada como dd/mm/aaaa
 Equipo1 y Equipo2 son los nombres de los equipos
 Si el partido quedó empatado no hay ni ganador, ni perdedor, por lo que no se
 escribe en ningún archivo
 Todas las salidas por pantalla, deben tener los mensajes apropiados
'''


# Ejercicio: Evaluando los resultados del Futbol

# Entrada
fecha: str
equipo1: str
equipo2: str
golesEquipo1: int
golesEquipo2: int

# Salida
porcentajeEmpatados: float
equipo1Mayor: str
equipo2Mayor: str  # Equipos participantes en partido con más goles

# Variables Auxiliares
diferenciaDeGoles: int
sumaDeGoles: int
partidosEmpatados: int
numeroDeEquipos: int
bandera: bool
mayorCantidaDeGoles: int

# Inicialización
bandera = True
partidosEmpatados = 0
numeroDeEquipos = 0

# Apertura de archivos
arch1 = open("juegos.txt", 'r')
arch2 = open("ganadores.txt", 'w')
arch3 = open("perdedores.txt", 'w')

# Ciclo de control para lectura de registros de la lista

for registro in arch1:
    linea = registro.split(',')
    fecha = linea[0]
    equipo1 = linea[1]
    equipo2 = linea[2]
    golesEquipo1 = int(linea[3])
    golesEquipo2 = int(linea[4])

    diferenciaDeGoles = golesEquipo1 - golesEquipo2

    # Validación de resultado del partido para impresión en el archivo
    # correspondiente

    if diferenciaDeGoles == 0:
        # Contador del número de partidos empatados
        partidosEmpatados = partidosEmpatados + 1
    elif diferenciaDeGoles < 0:
        arch2.write(f'{equipo2}, {golesEquipo2}\n')
        arch3.write(f'{equipo1}, {golesEquipo1}\n')
    elif diferenciaDeGoles > 0:
        arch2.write(f'{equipo1}, {golesEquipo1}\n')
        arch3.write(f'{equipo2}, {golesEquipo2}\n')

    # Detección del partido con mas goles

    sumaDeGoles = golesEquipo1 + golesEquipo2

    if bandera:
        equipo1Mayor = equipo1
        equipo2Mayor = equipo2
        mayorCantidaDeGoles = sumaDeGoles
        bandera = False
    elif sumaDeGoles > mayorCantidaDeGoles:
        equipo1Mayor = equipo1
        equipo2Mayor = equipo2
        mayorCantidaDeGoles = sumaDeGoles

    # Contador del número de equipos en la lista
    numeroDeEquipos += 1

porcentajeEmpatados = partidosEmpatados / numeroDeEquipos

print(f"Porcentaje de equipos que quedaron empatados: {porcentajeEmpatados:.2f}")

print(f"Equipos participantes en partido con más goles: {equipo1Mayor} y {equipo2Mayor}")

arch1.close()
arch2.close()
arch3.close()