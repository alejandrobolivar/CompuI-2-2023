'''
Declarar variables de entrada
n
x
'Declarar variables de salida
suma
'Declarar variables de proceso
termino
signo
numerador
denominador
fact
par
i
'''

# lectura de la cantidad de términos y de la variable de la serie

n = int(input("n: "))
x = float(input("x: "))

# Inicializar las variables
suma = 0
signo = 1
fact = 1
par = 1

# Proceso
for i in range(n):
    # Calcular cada elemento del termino
    if i == 0:
        termino = 1
    else:
        signo = (-1) ** i
        numerador = x ** (2 * i)
        fact *= i
        par = 2 * i
        denominador = par * fact
        # Calcular el termino
        termino = signo * numerador / denominador

    # Sumar el termino
    suma += termino
    print("Termino (" , i , ") = ", termino)

# Impresión de resultado
print("Suma=", suma)