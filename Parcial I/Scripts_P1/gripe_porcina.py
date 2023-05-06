'''
L A G R I P E P O R C I N A
En la actualidad la Organización Mundial de la Salud (OMS), tiene activada una
alerta de pandemia por el brote del virus de gripe porcina, que a partir del 30 de
abril de 2009 es llamado virus gripal A (H1N1). Para la fecha se han confirmado de
forma oficial un total 8480 casos, distribuidos en 39 países alrededor del mundo.
Considerando esta situación y que en Colombia y en Brasil, países vecinos, hay casos
confirmados recientemente, el Ministerio del Poder Popular para la Salud de
Venezuela activará un plan de detección de sospechosos de portadores del virus
gripal A(H1N1), para lo cual se le solicita a ud. que considerando la siguiente información correspondiente a
todos los pacientes en las instituciones de salud del país:

NOMBRE DEL PACIENTE, ESTADO AL QUE PERTENECE, TEMPERATURA, HEMOGLOBINA Y CANTIDAD DE GLÓBULOS
BLANCOS DEL PACIENTE

Desarrolle un programa que procese de un grupo de pacientes la información previamente indicada y
determine e imprima:
1. Si el paciente es sospechoso de ser portador del virus o no.
2. Porcentaje de pacientes sospechosos.
3. Estado del país donde se encontró el primer paciente sospechoso de tener el virus.
4. Cantidad de pacientes procesados hasta obtener el primer paciente sospechoso.
5. Temperatura promedio de los pacientes sospechosos.
Consideraciones:
Se considera que un paciente es sospechoso de ser portador del virus gripal A(H1N1), si sus valores son los
siguientes:
1.- la temperatura es mayor de 38 ºC,
2.- la hemoglobina está por debajo de 10 mg/dl y
3.- la cantidad de glóbulos blancos está por debajo de 4000
'''

cont_sosp = 0
cont_tot = 0
acum_temp = 0
resp='s'
while resp.lower() == 's' :
    nombre = input("nombre del paciente: ")
    estado = input("estado de procedencia: ")
    temperatura = float(input("temperatura corporal: "))
    hemoglobina = float(input("valor de la hemoglobina: "))
    globulos = int(input("valor de la cantidad de globulos blancos: "))
    cont_tot += 1  # cuenta todos los pacientes que se han ingresado
    if temperatura > 38 and hemoglobina < 10 and globulos < 4000 :
        cont_sosp += 1  # cuenta la cantidad de sospechosos
        acum_temp = acum_temp + temperatura  # suma todas las temperaturas de los pacientes sospechosos
        print("el paciente es sospechoso de tener el virus")  # p1
        if cont_sosp == 1:  # p3 y p4
            estado_1sosp = estado
            cant_1sosp = cont_tot
    else:
        print("el paciente no es sospechoso de tener el virus")  # p1

    resp = input("Desea agregar otro paciente? Si(s) no(n): ")

print("el primer sospechoso se encontró en el estado" , estado_1sosp)  # p3
print("la cantidad de pacientes procesados hasta conseguir el primer paciente sospechoso es de: ", cant_1sosp)  # p4
if cont_tot != 0:
    porc = (cont_sosp / cont_tot) * 100
    print("el porcentaje de pacientes sospechosos es de: ", porc)  # p2
else:
    print('No se procesaron pacientes')

if cont_sosp != 0:
    prom = (acum_temp/cont_sosp)
    print("el promedio de los pacientes sospechosos es de: ", prom)  # p5
else:
    print('No hubo pacientes sospechosos')