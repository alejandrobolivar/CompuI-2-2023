'''
En vista del próximo regreso a clase, como todos los años la
universidad realizará la acostumbrada feria del libro, para este año a
las editoriales que participarán en la feria se les exigió que emitieran
una lista de todos los libros que estos colocarán a la venta indicando
lo siguiente:
Editorial Representante
y por cada libro a vender en líneas separadas:
Título del libro, Género, Año de publicación, Cantidad en existencia y Precio
La universidad le pide a usted que dada esta información de todos los vendedores un archivo de datos de
nombre FILUC2008.dat la procese y determine e imprima:

Por cada libro:
1) Editorial, Título y Si podrá o no ser vendido en la próxima feria del Libro FILUC2008. (1 pto / 9 ptos )
Por cada Editorial:
2) Porcentaje de libros aceptados. ( 1 pto / 9 ptos )
Para todas las editoriales:
3) Título del Libro más costoso entre los aceptados y empresa editorial que lo expenderá. ( 2 ptos / 9 ptos )
4) Cantidad de editoriales cuyo porcentaje de libros aceptados sea superior a 75%. (1 pto / 9 ptos)

CONSIDERACIONES:
a) El género será: ‘I’ = Investigaciones o Publicaciones; ‘L’= Literatura; ‘T’ = Tecnológico y científicos; ‘O’ = Otros.
b) Sólo se podrán vender libros publicados en los últimos 5 años.

# Variables de entrada
editorial: str
representante: str
titulo_libro: str
genero: str
anho: int
cantidad: int
precio: float

# Variables de salida
porc_aceptados: float
libro_maxcosto: str
edit_maxcosto: str
cant_editoriales: int = 0

# Variables de proceso
bandera: bool  # Auxiliar para cálculo del libro mas costoso
cent: int  # Variable para controlar el ciclo interno
cont_t: int  # Contador de libros totales
cont_p: int  # Contador de libros permisibles a la venta para calculo del porc
precio_max: float  # Variable comparador para determinar el libro mas costoso
'''

# Apertura de archivos
arch = open("filuc2008.txt", 'r')
# Inicializacion de acumuladores y contadores
bandera = True

while True:
    linea = arch.readline()

    if linea == '':  # Fin del archivo
        break

    else:
        lista_ext = linea.split(',')
        editorial = lista_ext[0]
        representante = lista_ext[1].split('\n')

        # Inicializacion de contadores para cada editorial
        cont_p = 0
        cont_t = 0

        cent = 0

        while cent == 0:
            lista_int = arch.readline().split(',')
            titulo_libro = lista_int[0]
            genero = lista_int[1]
            anho = int(lista_int[2])
            cantidad = int(lista_int[3])
            precio = float(lista_int[4])
            cent = int(lista_int[5])
            print(cent)

            cont_t += 1

            # Impresiones por cada libro
            print(f"Titulo del libro: {titulo_libro} editorial: {editorial} .")

            if anho <= 2003:
                print("No puede ser vendido")
            else:
                print("Sí puede ser vendido")
                cont_p = cont_p + 1     # Contador de libros aceptados

                # Calculo del libro mas costoso que puede ser vendido
                if bandera:
                    libro_maxcosto = titulo_libro
                    precio_max = precio
                    edit_maxcosto = editorial
                    bandera = False
                elif precio_max < precio:
                    libro_maxcosto = titulo_libro
                    precio_max = precio
                    edit_maxcosto = editorial

    # Calculo de porcentaje
    if cont_t > 0:
        porc_aceptados = (cont_p / cont_t) * 100

        # Impresiones por cada editorial
        print(f"Editorial: {editorial} Porcentaje de libros aceptados {porc_aceptados:.2f}")

    if porc_aceptados > 75:
        cant_editoriales += 1

print("____________________________________")
print(f"Libro mas costoso: {libro_maxcosto}")
print(f"Editorial {edit_maxcosto}")
print(f"Cantidad de editoriales cuyo porcentaje de libros aceptados sea superior a 75% {cant_editoriales}")
arch.close()
