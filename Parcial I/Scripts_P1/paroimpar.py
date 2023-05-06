# Entrada del dato
n = int(input('De un valor entero: '))
# Procesamiento y salida de datos
if n == 0:
    print(n, ' No es par ni impar')
elif n % 2 != 0:
    print(n, ' Es Impar')
else:
    print(n, ' Es Par')

# Fin del programa
input('Pulse una tecla para finalizar... ')  # Pausa
