'''
'Declaración de Variables:
'Variables de entrada (Qué tengo?)
Dim H As Single 'Número de variable de la serie
Dim M As Integer 'Términos
'Variables de salida (Qué quiero?)
Dim suma As Single 'Suma de los términos
Dim Termino As Double 'Valor de cada termino
'Variables de proceso (Cómo lo logro?)
Dim i As Integer 'Controlador del ciclo
Dim signo As Integer 'Signo del termino
Dim suma_impares As Integer 'Números del numerador
Dim suma_pares As Integer 'Números del denominador
Dim numerador As Double 'Valor de todo el numerador
Dim denominador As Double 'Valor de todo el denominador
'''

# Lecturas correspondientes
# Se leen los valores de número de variable de la serie (h) y términos (m)

h = float(input("Introduzca el valor de la variable de la serie (h): "))
m = int(input("Introduzca el valor del número de términos (m): "))

# Inicializaciones correspondientes
suma = 0
signo = -1
suma_impares = 0
suma_pares = 0

# Determinación de los términos de la serie
for i in range(m):  # Para los primeros m términos
    # Cálculo de cada elemento del término
    suma_impares += (2 * i + 1)
    suma_pares += (2 * i + 2)
    numerador = signo * h ** (i + 1) * suma_impares ** m
    if i % 2 != 0:  # Los términos pares no tienen factorial
        denominador = suma_pares
    else: # Los términos impares tienen factorial
        factorial = 1
        for j in range(suma_pares):
            factorial *= j + 1

        denominador = factorial

    termino = numerador / denominador  # Determinación del término e impresión
    print("Término: ", i + 1, " = ", termino)
    signo = 1  # El resto de los términos son positivos
    suma += termino  # Se acumula la suma

# Se imprime la suma
print("La suma de los ", m, " primeros términos es: ", suma)