'''
En la actualidad la Organización Mundial de la Salud (OMS), tiene
activada una alerta de pandemia por el brote del virus de fiebre
porcina, que a partir del 30 de abril es llamado virus gripal A (H1N1).
Considerando que ya tenemos casos confirmados en el país, el
Ministerio del Poder Popular para la Salud activará un plan de
detección de sospechosos de portadores del virus gripal A(H1N1),
para lo cual se registra en el archivo de datos fiebre.dat, la siguiente
información correspondiente a todos los pacientes en las instituciones
de salud del país:
Nombre del Paciente, Nombre de la Institución Asistencial,
Temperatura del Paciente, Hemoglobina y Cantidad de Glóbulos
Blancos
Desarrolle un programa que procese la información antes mencionada y genere 2 archivos llamados
sospechosos.dat y nosospechosos.dat, en donde se almacenen los datos de los pacientes sospechosos y
no sospechosos respectivamente. Además determine e imprima por pantalla:
 Porcentaje de pacientes no sospechosos.
 Nombre del paciente e institución donde se localiza el paciente con mayor cantidad de glóbulos
blancos.
Consideraciones:
 Se considera que un paciente es sospechoso de ser portador del virus gripal A(H1N1), si su valores
son los siguientes: la temperatura es mayor de 38 °C, la hemoglobina está por debajo de 10 mg/dl y
la cantidad de glóbulos blancos esté por debajo de 4.000
'''

#  VARIABLES DE ENTRADA
NOMP: str = '' #  NOMBRE DEL PACIENTE
NOMI: str #  NOMBRE DE LA INSTITUCION
TEMP: float #  TEMPERATURA DEL PACIENTE
HEM: float #  HEMOGLOBINA DEL PACIENTE
GB: int #  CANTIDAD DE GLOBULOS BLANCOS
#  VARIABLES DE PROCESO
CNS: int #  CONTADOR DE PACIENTES NO SOSPECHOSOS
CP: int #  CONTADOR DE PACIENTES
BAND: int #  BANDERA PARA DETERMINAR EL PACIENTE CON MAYOR CANTIDAD DE GLOBULOS BLANCOS
GBMAY: int #  AUXILIAR PARA DETERMINAR EL PACIENTE CON MAYOR CANTIDAD DE GLOBULOS BLANCOS
#  VARIABLES DE SALIDA
PORNS: float #  PORCENTAJE DE PACIENTES NO SOSPECHOSOS
NPMAY: str #  NOMBRE DEL PACIENTE CON MAYOR CANTIDAD DE GLOBULOS BLANCOS
NIMAY: str #  NOMBRE DE LA INSTITUCION DONDE ESTA EL PACIENTE CON MAYOR CANTIDAD DE GLOBULOS BLANCOS
#  APERTURA DEL ARCHIVO DE ENTRADA
arch1 = open("FIEBRE.DAT", 'r')
#  APERTURA DE LOS ARCHIVOS DE SALIDA
arch2 = open("SOSPECHOSOS.DAT", 'w')
arch3 = open("NOSOSPECHOSOS.DAT", 'w')
#  INICIALIZACION DE ACUMULADORES CONTADORES Y BANDERAS
BAND = True
CNS = 0
CP = 0
#  COMO NO SE CONOCE LA CANTIDAD DE DATOS DE LA LISTA UTILIZAMOS UN CICLO WHILE

for registro in arch1:
    linea = registro.split(',')
    #  LECTURA DE LOS DATOS DEL ARCHIVO
    NOMP = linea[0]
    NOMI  = linea[1]
    TEMP  = float(linea[2])
    HEM = float(linea[3])
    GB = int(linea[4])
    #  CONDICION PARA SABER SI EL PACIENTE ES SOSPECHOSO
    
    if TEMP > 38 and HEM < 10 and GB < 4000:
        #  IMPRIMIMOS LOS DATOS DEL PACIENTE EN EL ARCHIVO SOSPECHOSOS.DAT
        arch2.write(f'{NOMP} {NOMI} {TEMP} {HEM} {GB}\n')
    else: #  SI EL PACIENTE ES NO SOSPECHOSO
        #  IMPRIMIMOS LOS DATOS DEL PACIENTE EN EL ARCHIVO NOSOSPECHOSOS.DAT
        arch3.write(f'{NOMP} {NOMI} {TEMP} {HEM} {GB}\n')
        # CONTAMOS LA CANTIDAD DE PACIENTES NO SOSPECHOSOS
        CNS += 1

    #  CONTAMOS LA CANTIDAD DE PACIENTES
    CP += 1
    #  DETERMINACION DEL PACIENTE CON MAYOR CANTIDAD DE GLOBULOS BLANCOS
    if BAND:
        NPMAY = NOMP
        NIMAY = NOMI
        GBMAY = GB
        BAND = False
    elif GBMAY < GB:
        NPMAY = NOMP
        NIMAY = NOMI
        GBMAY = GB

#  DETERMINACION DEL PORCENTAJE DE PACIENTES NO SOSPECHOSOS
PORNS = (CNS / CP) * 100
#  IMPRESION DEL PORCENTAJE DE PACIENTES NO SOSPECHOSOS
print(f"EL PORCENTAJE DE PACIENTES NO SOSPECHOSOS ES: {PORNS} %")
#  IMPRESION DE LOS DATOS DEL PACIENTE CON MAYOR CANTIDAD DE GLOBULOS BLANCOS
print(f"EL PACIENTE: {NPMAY} DEL INSTITUTO: {NIMAY} ES EL QUE TIENE MAYOR CANTIDAD DE GLOBULOS BLANCOS")

#  CIERRE DE LOS ARCHIVOS DE DATOS
arch1.close()
arch2.close()
arch3.close()