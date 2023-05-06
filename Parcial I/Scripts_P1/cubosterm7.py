c = 0
for i in range(1000):
    ultimo_digito = (i ** 3) % 10
    if ultimo_digito == 7:
        c = c + 1
print (c)
