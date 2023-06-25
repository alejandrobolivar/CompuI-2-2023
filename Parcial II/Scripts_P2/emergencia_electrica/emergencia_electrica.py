'''
Pregunta 2. Emergencia Eléctrica, evaluemos el consumo eléctrico 
El pasado 09 de febrero fue decretado oficialmente la emergencia eléctrica en
Venezuela, lo cual confirmó la crisis eléctrica que se está viviendo en el país, debido a
esto las comunidades están evaluando su consumo eléctrico; para ello se tiene la
información del consumo de los suscriptores agrupados por zonas en el archivo
consumos.txt.
Esta información se organiza en el archivo de la siguiente manera:
Zona y número de suscriptores
Y para cada suscriptor se tiene
Tipo de suscriptor, Número de Contrato, Lectura inicial y final del medidor en KWh
Desarrolle un programa, que procese la información del archivo
consumos.txt y genere dos nuevos archivos de nombres Residencial.txt y
comercial.txt, los cuales deben contener Número del contrato y Consumo eléctrico,
de los suscriptores de tipo residencial y comercial respectivamente.
Además se pide que imprima por pantalla lo siguiente:
1. Cantidad de usuarios de alto consumo por zona
2. Promedio de consumo de los usuarios de tipo residencial en el país
3. Zona con mayor consumo eléctrico
Consideraciones:
• El Tipo de Suscriptor puede ser: 1 para residencial y 2 para comercial
• El consumo eléctrico se determina como la diferencia entre las lecturas del medidor
• Se consideran usuarios de alto consumo aquellos cuyo consumo sea superior a 500 KWh
'''

# Pregunta 2. Exámen Parcial II. Computación I. Periodo 2/2009

zona: str
zonaMayor: str
num_suscriptores: int
nombreArchivoEntrada: str
nombreArchivoResidencial: str
nombreArchivoComercial: str
tipo: int
inicial: int
final: int
contResidencial: int
contrato: str
totalConsumo: int
i: int
consumo: int
altoConsumo: int
sumaConsumo: int
mayor: int
promedio: float
esPrimeraZona: bool

arch1 = open('consumos.txt', 'r')
arch2 = open('residencial.txt', 'w')
arch3 = open('comercial.txt', 'w')

sumaConsumo = 0
contResidencial = 0
esPrimeraZona = True

while True:  # Lista de Zonas
    linea = arch1.readline()
    if linea == '':
        break
    list_ext = linea.split(',')
    # Lectura de datos de la zona
    zona = list_ext[0]
    num_suscriptores = int(list_ext[1])

    altoConsumo = 0
    totalConsumo = 0

    for _ in range(num_suscriptores):  # Suscriptores por zona
        linea = arch1.readline()
        list_int = linea.split(',')
        # Lectura de datos del suscriptor
        tipo = int(list_int[0])
        contrato = list_int[1]
        inicial = int(list_int[2])
        final = int(list_int[3])

        # Cálculo del consumo
        consumo = final - inicial

        # Acumulador del consumo por zona
        totalConsumo = totalConsumo + consumo

        match tipo: # Dependiendo del tipo de suscriptor hacer...

            case 1:  # Residencial, archivo número 2
                # Imprimir datos del suscriptor residencial en el archivo correspondiente
                arch2.write(f'CONTRATO: {contrato} CONSUMO: {consumo}\n')
                # Cálculos necesarios para determinar, fuera del ciclo, el promedio de consumo residencial
                sumaConsumo += consumo
                contResidencial += 1

            case 2:  # Comercial, archivo número 3
                # Imprimir datos del suscriptor comercial en el archivo correspondiente
                arch3.write(f'CONTRATO: {contrato} CONSUMO: {consumo}\n')

        # Contador de suscriptores de alto consumo
        if consumo > 500: altoConsumo += 1

    # Imprimir por pantalla la cantidad de suscriptores de alto consumo por zona.
    # Se utiliza el tercer parámetro Iif(altoConsumo>1,"s",""), con la finalidad de
    # imprimir la "s" de la palabra usuario, si la cantidad es mayor que uno.
    print(f'Hay {altoConsumo} usuario{"s" if altoConsumo > 1 else ""} de alto consumo en la zona {zona}')

    # Cálculo de Zona con Mayor Consumo
    # Si es la primera zona, el valor de esPrimeraZona será verdadero
    if esPrimeraZona:
        mayor = totalConsumo
        zonaMayor = zona
        esPrimeraZona = False # Ya dejó de ser la primera zona
    elif totalConsumo > mayor:
        mayor = totalConsumo
        zonaMayor = zona

# Chequeo en caso de que no hayan suscriptores residenciales.
if contResidencial != 0:
    promedio = sumaConsumo / contResidencial
    print(f'El promedio de consumo de los suscriptores residenciales es {promedio:.2f}')
else: # No hay suscriptores residenciales
    print("No hay suscriptores residenciales")

print(f'La zona con mayor consumo eléctrico es {zonaMayor}')

arch1.close()
arch2.close()
arch3.close()

# Necesario para que se detenga la ejecución en pantalla.
# Si lo desea lo puede eliminar.
input("Pulse cualquier tecla para terminar...")