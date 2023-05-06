
'''
La Unidad de Radiología X-Ray realiza cuatro tipos de estudios radiológicos: Cabeza, Tórax, Columna y Extremidades. Con el objeto de estandarizar el precio de los estudios, se decide ajustarlos de acuerdo al valor de la Unidad Tributaria definida por el SENIAT cuyo valor para el año en curso se establece como una constante equivalente a 127 Bs por cada UT. La siguiente tabla muestra los costos de cada examen:
Estudio Realizado	Costo
Cabeza	2.75 UT
Tórax	2.50 UT
Columna	5.25 UT
Extremidades	2.25 UT 
Al final de una jornada de trabajo de la Unidad, se registra en una lista los datos de los N estudios realizados, donde para cada uno se tiene: 
Cédula, Nombre y Edad del Paciente, y el Tipo de estudio realizado (1=Cabeza, 2=Tórax, 3=Columna, 4=Extremidades)
Elabore un programa, que lea la lista con los datos registrados de los N estudios y determine e imprima:
Para cada Estudio:
Nombre del Paciente, Monto en Bs. del estudio sin IVA, el monto del IVA (8%) y El Monto Total que canceló el paciente.
Para todos los Estudios:
Suma total recaudada en Bs., sin tomar en cuenta el IVA, y el monto total en Bs. cobrados por IVA
Promedio de Monto en Bs. sin IVA de los pacientes que se realizaron Estudios de Cabeza o Columna, y cuya edad sea mayor a 40 años.
Porcentaje de Personas con edad comprendida entre 45 y 52 años
'''
# Declaración de Constantes
UT = 75
# Inicialización
suma = 0
cont = 0
totalsiniva = 0
totaliva = 0
promedio = 0
porcentaje = 0
contedad = 0
# Lectura de la cantidad de estudios
n = int(input("Cantidad de estudios realizados:"))
# Proceso
for _ in range(n):
    #Lectura de datos de entrada
    cedula = input("Cédula:")
    nombre = input("Nombre:")
    edad = int(input("Edad:"))
    tipoestudio = int(input("Tipo de Estudio:"))
    if tipoestudio == 1:
        monto = 2.75 * UT
    elif tipoestudio == 2 :
        monto = 2.5 * UT
    elif tipoestudio == 3 :
        monto = 5.25 * UT
    else:
        monto = 2.25 * UT

    iva = monto * 0.08
    total = monto + iva

    # Pregunta 1
    print("Nombre= " , nombre , "Monto sin IVA= " , monto , "IVA (8%)= " , iva , "Total= " , total)

    # Pregunta 2
    totalsiniva += monto
    totaliva += iva

    # Pregunta 3
    if tipoestudio == 1 or tipoestudio ==3 and edad > 40:
        suma += monto
        cont += 1

    # Pregunta 4
    if edad > 45 and edad < 52:
        contedad += 1

# Salida de Datos
# Pregunta 2
print("Total Recaudado sin IVA=" , totalsiniva)
print("Monto Total cobrado por IVA (8%)=" , totaliva)

#Pregunta 3
if cont !=  0:
    promedio = suma / cont
    print("Promedio de Monto en Bs sin IVA de Estudios 1 o 3, con edad mayor a 40 años=" , promedio)
else:
    print("No hubo pacientes con estudios de cabeza o columna mayor de 40 años")

# Pregunta 4
porcentaje = contedad * 100 / n
print("El porcentaje de personas con edad comprendida entre 45 y 52 años es = " , porcentaje)