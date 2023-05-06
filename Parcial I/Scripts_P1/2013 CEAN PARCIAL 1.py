'''
Un cybercafé es un local público donde se ofrece a los clientes acceso a
Internet y en algunos locales, servicio de cafetería.
El cybercafé “Los Pobresores” necesita controlar las operaciones del
negocio, así que para lograr este objetivo se evaluaron en la recepción del
local los siguientes datos de un grupo de N clientes:
NOMBRE DEL CLIENTE, EDAD, HORA Y MINUTOS DE LLEGADA,
y de PODER hacer uso de los servicios del local se lee además,
EL TIEMPO DE CONEXIÓN EN MINUTOS Y SI PIDIÓ SERVICIO DE CAFETERÍA (“SI”/”NO”)
Se debe desarrollar una aplicación de consola en VB2010 que procese los datos suministrados y determine
e imprima la siguiente información:
Por cada cliente:
1) Indique si pudo entrar o no al cibercafé, en caso de entrar, indique a qué hora salió (en horas y
minutos), de no entrar indique por qué razón no pudo entrar, si por la edad o porque el cybercafé ya
cerró.
2) Si el cliente puede hacer uso de los servicios, pero llegó antes de la hora de abrir el cybercafé, indique
cuantos minutos debe esperar para poder entrar y considere el cálculo para la hora de salida en el
punto anterior.
Para todos los clientes:
3) Nombre y edad del cliente que llegó al cybercafé después de las 12:00 (720 min del día) y salió después
del cierre 17:00 (1020 min del día), con el mayor tiempo de conexión, de haber más de uno con la
misma condición, indique el último en procesar.
4) Porcentaje de clientes que esperaron que abriera el cybercafé y pudieron hacer uso de nuestros
servicios con respecto a los clientes atendidos en el día.
5) Cuantos clientes se procesaron antes de atender el primero que pidió servicio de cafetería y cuantos
pidieron ese servicio después de él.
CONSIDERACIONES:
a) El cibercafé abre a las 8:00 (480 min del día) y cierra a las 17:00 (1020 min del día).
b) Todo cliente que llega antes de abrir el local necesita hacer uso del local y espera que abra.
b) Los clientes deben tener más de 17 años para poder entrar al cybercafé.
c) Los clientes son procesados según la hora y minutos del día que van llegando, así que se atienden un
máximo de N clientes hasta que aparezca el primer cliente que llegue después del cierre del
cybercafé.
d) Las horas se manejan en formato de 24 horas (formato militar).
'''

'''
# Variables de entrada
Nombre, serv_caf : str
N, edad, h_llegada, m_llegada, min_conexion : int
# Variables de proceso
cant_proc, cont_espera, mint_llegada, min_espera : int
cont_4, cont_5_antes, cont_5_despues, band_3, band_5 : int
# Variables de salida
hora_salida, min_salida, mint_salida, edad_mayor, min_conex_mayor : int
nombre_mayor : str
porcentaje_4 : float
'''

# Inicialización de contadores y banderas
cant_proc = 0
cont_espera = 0
cont_4 = 0
band_3 = 0
band_5 = 0
cont_5_antes = 0
cont_5_despues = 0
mint_llegada = 0
edad_mayor = 0
nombre_mayor = ""
# Lectura de clientes a procesar HASTA QUE CIERRE EL LOCAL
n = int(input("Introduzca la cantidad de clientes a procesar: "))
# Ciclo DO debido a que debo cumplir 2 condiciones para estar dentro del ciclo. NO CONFUNDIR CON CICLO FOR
# Debemos recordar que atendemos a los n clientes siempre y cuando lleguen antes de la hora de cierre del local.
while (cant_proc < n and mint_llegada <= 1020):
    nombre = input("Introduzca el nombre del cliente: ")
    edad = int(input("Introduzca la edad del cliente: "))
    h_llegada = int(input("Introduzca la HORA de llegada: "))
    m_llegada = int(input("Introduzca los MINUTOS de llegada: "))
    # Incremento del contador de clientes procesados, sin importar si lograron o no
    # hacer uso de los servicios del cyber
    cant_proc += 1
    mint_llegada = h_llegada * 60 + m_llegada  # Convierte la hora de llegada a minutos totales
    if edad < 17:  # Verificación de si puede o no entrar debido a la edad
        print("No pudo ingresar al cyber debido a que no cumple con la edad mínima.")
    else:
        if mint_llegada >= 1020:  # Verificación de si puede o no entrar debido a la hora de llegada
            print("No pudo ingresar al cyber debido a que llegó luego de la hora de cierre del local.")
        else:
            cont_4 += 1  # incremento la cantidad de cliente que pudieron entrar y hacer uso de los servicios
            # Lecturas de la información para los que SI PUDIERON ENTRAR
            min_conexion = int(input("Introduzca el tiempo de conexión en minutos: "))
            serv_caf = input("¿El cliente solicitó servicio de cafetería? SI o NO: ")
            if mint_llegada < 480:  # Comprobar las personas que debieron esperar a que abriera el sistema
                min_espera = 480 - mint_llegada
                cont_espera += 1
                hora_salida = (480 + min_conexion) // 60
                min_salida = (480 + min_conexion) % 60
                print("El cliente tuvo que esperar: " , min_espera , "min, para poder entrar al local")
            else:
                hora_salida = (mint_llegada + min_conexion) // 60
                min_salida = (mint_llegada + min_conexion) % 60
            print("Pudo entrar al cyber café y salió a las: " , hora_salida , ":" , min_salida)
            mint_salida = (hora_salida * 60) + min_salida
            print(mint_llegada, mint_salida)
            if mint_llegada > 720 and mint_salida > 1020:  # Verificación condición de la pregunta 3
                if band_3 == 0:
                    nombre_mayor = nombre
                    edad_mayor = edad
                    min_conex_mayor = min_conexion
                    band_3 = 1
                elif min_conexion >= min_conex_mayor:
                    nombre_mayor = nombre
                    edad_mayor = edad
                    min_conex_mayor = min_conexion
            if serv_caf.upper() == "SI":  # Verificación de la condición de la pregunta 5
                if band_5 == 0:
                    cont_5_antes = cant_proc
                    band_5 = 1
                else:
                    cont_5_despues += 1
if band_3 == 1:
    print("La última persona que llegó luego de las 12:00 y salió después de las 17:00, fue: " , nombre_mayor , " y su edad es: " , edad_mayor)
else:
    print("Nadie llegó luego de las 12:00 y salió después de las 17:00")
if cont_4 > 0:  # Validación del denominador para la respuesta 4
    porcentaje_4 = cont_espera / cont_4 * 100
    print("El porcentaje de clientes que esperaron y que hicieron uso de los sevicios es: " , porcentaje_4 , "%")
else:
    print("No se atendieron clientes en la jornada")
if band_5 != 0:
    print("Se procesaron " , cont_5_antes , " personas antes de que alguna solicitara servicio de cafetería")
    print("Se procesaron " , cont_5_despues , " personas luego de que alguna solicitara servicio de cafetería")
else:
    print("Nadie solicitó servicio de cafetería")