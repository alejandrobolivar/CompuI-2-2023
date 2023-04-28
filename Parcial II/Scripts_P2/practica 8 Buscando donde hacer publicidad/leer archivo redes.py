with open('redes.txt','r') as arch1:
    contenido = arch1.readlines()
    linea = 0
    w = int(contenido[linea])
    linea += 1

    for _ in range(w):
        lista = contenido[linea].split(',')
        linea += 1

        nombre = str(lista[0])
        genero =str(lista[1])
        edad = int(lista[2])
        red = int(lista[3])

        print('%s, %s, %d, %d' % (nombre,  genero, edad, red))