
with open('ordenes 2.txt','r') as arch1:
    contenido = arch1.readlines()
    # cantidad de elementos de la lista externa desconocida
    linea = 0  # Posición del primer elemento de la lista externa

    while linea < len(contenido):  # CICLO QUE PROCESA LAS ORDENES DE COMPRA (lista externa)
        # LECTURA DE LAS ORDENES
        listaext = contenido[linea].split(',')
        linea += 1  # se incrementa el contador de líneas de contenido
        noc = int(listaext[0])
        nombre =  listaext[1]
        m = int(listaext[2])  # cantidad de elementos de la lista interna
        print('%d, %s, %d' % (noc, nombre, m))

        for _ in range(m): # CICLO QUE PROCESA LOS RENGLONES DE ESP (lista interna)
            listaint = contenido[linea].split(',')
            linea += 1  # se incrementa el contador de líneas de contenido
            area = float(listaint[0])
            l = float(listaint[1])
            a = float(listaint[2])
            monto = float(listaint[3])
            print('%.2f, %.2f, %.2f, %.2f' % (area, l, a, monto))