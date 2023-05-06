print ('Ingrese diez números positivos')

mayor = -1
for i in range(10):
    n = int(input())
    if n > mayor:
        mayor = n

print ('El mayor es ', mayor)
