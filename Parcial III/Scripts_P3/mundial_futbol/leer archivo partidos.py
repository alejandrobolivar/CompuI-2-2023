# Manejo de Archivos
with open("partidos.txt", "r") as arch1:
    contenido = arch1.readlines()
    linea = 0
    cp = int(contenido[linea])  # cantidad de partidos
    linea += 1  # Posición del siguiente elemento

    # Ciclo de lectura
    for i in range(1, len(contenido)):  # CICLO QUE PROCESA los países

        lista = contenido[linea].split(',')
        linea += 1

        nom = lista[0]
        print(nom)

        for i in range(1, cp + 1):
            gf = int(lista[2*i-1])
            gc = int(lista[2*i])
            print('%d, %d' % (gf, gc))
