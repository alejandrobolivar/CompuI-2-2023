# Apertura de los archivos

# Archivo de lectura
arch1 = open('datos.dat', 'r')
# Archivos a generar
arch2 = open('aprobados.dat', 'w')
arch3 = open('reprobados.dat', 'w')

# Recorrido del archivo
for registro in arch1:
    # Devuelve una lista con los campos del registro
    linea = registro.split(',')
    print(linea)

    #Procesar elementos:
    #Utilizar archivo para leer la lista
    nombre = linea[0]     # Nombre del estudiante
    print(nombre)
    cedula = linea[1]     # Cédula del estudiante
    print(cedula)
    nota = int(linea[2])  # Nota del estudiante
    print(nota)
    if nota >= 10:  # Está aprobado
        arch2.write(f'{nombre}, {cedula}' + '\n')
    else:  # esta reprobado
        arch3.write(f'{nombre}, {cedula}' + '\n')

# Cerrar archivos
arch1.close()
arch2.close()
arch3.close()

# Escritura de resultados
print('Los resultados están en los archivos aprobados y reprobados.dat en el directorio de trabajo')