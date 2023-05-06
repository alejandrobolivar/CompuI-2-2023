# Cálculo de la suma de los primeros n números
n = int(input('Entra un número natural: '))
i = 1
suma = 0
while i <= n:
    suma = suma + i
    i = i + 1
print('La suma de los números naturales hasta', n,'es', suma)
