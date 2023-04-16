'''
YouTube, es un sitio web en el cual los usuarios pueden subir y compartir
videos. La empresa desea realizar algunos estudios relacionados con las
visitas y los videos más visitados en el sitio web, con el fin de mejorar el
servicio que presta a todos sus visitantes. Diariamente se lleva un registro
de los datos de cada video conformado por:

Código, Tipo, Cantidad de visitas del día anterior, Cantidad de visitas del día actual

YouTube, le ha contratado a Ud. para que desarrolle un programa que procese la información indicada anteriormente
y determine e imprima:

Para cada video:
1. Un mensaje que indique si el video está entre los favoritos o no.

Para todos los videos:
2. ¿Cuántos videos están entre los favoritos?
3. Porcentaje de videos de música con respecto al total de videos registrados
4. Código del video con el mayor incremento de visitas. Si existe más de un video con el mismo mayor incremento, indique el
que tiene la mayor cantidad de visitas del día anterior

Consideraciones:
a) El tipo de video es: 1= Música, 2= Comedia, 3=Deportes, 4= Cine.
b) El video está entre los favoritos si se mantiene o incrementa la cantidad de visitas

'''

# Inicializacion de variables

resp = 2
contfav = 0
c1 = 0
c = 0
band = 0
mayor_inc = 0
incremento = 0

# Entrada de Datos
while resp == 2:
    codigo = input('Ingrese el Codigo:  ')
    tipo = int(input('Que tipo de video es: ? 1= Musica, 2= Comedia , 3= Deporte , 4= Cine:  '))
    visitas_ayer = int(input('Ingrese la cantidad de visitas del dia anterior:  '))
    visitas_hoy = int(input('Ingrese la cantidad de visitas del dia actual:  '))
    
    c += 1
    incremento = visitas_hoy - visitas_ayer
    
    if incremento > 0:  # P1. Un mensaje que indique si el video está entre los favoritos o no.
        contfav += 1  # P2. ¿Cuántos videos están entre los favoritos?
        print('Este video esta entre los favoritos')
    else:
        print('No esta entre los favoritos')
        
    if tipo == 1:  # Música
        c1 += 1
    
    if band == 0:  # P4. Código del video con el mayor incremento de visitas.
        mayor_inc = incremento
        mayor_visitas_ayer = visitas_ayer
        codigom = codigo
        band = 1
    elif incremento > mayor_inc:
        mayor_inc = incremento
        codigom = codigo
    elif incremento == mayor_inc and visitas_ayer > mayor_visitas_ayer:
        codigoM = codigo
        
    resp = int(input('Desea procesar otra persona: ? 1=No , 2=Si '))

print('La cantidad de video favoritos es = ', contfav)

if c > 0:
	print('El porcentaje de video de musica es = ', (c1/c)*100)  # P3. Porcentaje de videos de música con respecto al total de videos registrados
else:
    print('No se vieron videos de musica')

if band != 0:
    print('el Codigo del video con el mayor incremento de visitas es = ', codigom)
else:
	print('Ningun video tuvo un incremento')