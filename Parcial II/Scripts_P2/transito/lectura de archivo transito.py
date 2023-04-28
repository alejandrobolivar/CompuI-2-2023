# Manejo de archivos
with open("datostransito.txt", 'r') as arch1:
    # Proceso
    for registro in arch1:
        # lectura de datos
        contenido = registro.split(',')

        nombre = contenido[0]
        genero = int(contenido[1])
        hora = int(contenido[2])
        velocidad = float(contenido[3])

        print('%s, %d, %d, %.2f' % (nombre,  genero, hora, velocidad))