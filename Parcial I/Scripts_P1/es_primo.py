# Programa que determina si un número es primo o no
n = int(input('Entra un número natural: '))
d = 2
un_divisor = True  # Si hay un divisor el número NO es primo
while d < n and un_divisor:
    if n % d == 0:
        un_divisor = False  # Se busca algún divisor
    d = d + 1
print('¿Es primo? ', un_divisor)
