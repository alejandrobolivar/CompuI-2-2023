'''Buscando donde hacer publicidad
Con la intención de hacer la web más social se han
creado múltiples aplicaciones o sitios en Internet que
permiten compartir información y establecer
comunicación entre grupos de personas, estos sitios
son denominados REDES SOCIALES. Una empresa
de publicidad cuyo lema es “las empresas que invierten
en publicidad, son las empresas que permanecen en la
mente de las personas”, quiere evaluar la posibilidad de
colocar publicidad en alguna de las tres redes
sociales que considera de mayor uso o más
comunes. Para ello se realiza una encuesta a un
conjunto W personas a quienes se les solicita
suministren la siguiente información:
NOMBRE, GÉNERO, EDAD Y RED SOCIAL MÁS
UTILIZADA
Desarrolle un programa que procese la información,
almacenada en un archivo de nombre REDES.TXT y
genere dos archivos de nombre USAREDSOCIAL.TXT
y NOLASENCUESTADAS.TXT, con los nombres de los
usuarios que usan alguna de las tres redes sociales
consideradas en el estudio o los que no usan ninguna de las redes sociales consideradas en el
estudio respectivamente, además determine e imprima por pantalla:
1.- Cantidad de personas que utilizan cada uno de las tres principales redes sociales
considerados en la encuesta.
2.- Porcentaje de personas que utilizan alguna de las tres principales redes sociales
considerados en la encuesta
3.- Nombre y edad del primer usuario procesado que usa hi5
4.- En cuál de las tres redes sociales sería más rentable invertir en publicidad.
Consideraciones:
o El género se tomará como 1 =Femenino y 2 = Másculino
o Los valores para tipo de red social más utilizada son 1 =Facebook, 2 =Myspace, 3=Hi5 y
4=Ninguno u otro
o Mientras más usuarios usen una red social, esta se considera más rentable para hacer
publicidad.
'''

with open('redes.txt', 'r') as archivo, open("usaredsocial.txt", 'w') as arch1, open("nolasencuestadas.txt", 'w') as arch2:
    cont_face = 0
    cont_hi = 0
    cont_space = 0
    cont = 0
    nombre_primero_hi = ''
    band = True
    cont_pr = 0
    contenido=archivo.readlines()
    for i in range(len(contenido)):
        linea = contenido[i].split(",")
        nombre = linea[0]
        genero = int(linea[1])
        edad = int(linea[2])
        red_social = int(linea[3])
        if 0 < red_social < 4:
            cont_pr += 1  # p2
            if red_social == 1:
                cont_face += 1
                arch1.write(nombre)
            elif red_social == 2:
                cont_space += 1
                arch1.write(nombre)
            elif red_social == 3:
                cont_hi += 1
                if band:  # p3
                    nombre_primero_hi = nombre
                    edad_primer = edad
                    band = False
            arch1.write(nombre)
        else:  # no utiliza red social
            cont += 1
            arch2.write(nombre)
    print("la cantidad de personas que utilizan facebook es: ", cont_face)  # p1
    print("la cantidad de personas que utilizan myspace es: ", cont_space)
    print("la cantidad de personas que utilizan hi5 es: ", cont_hi)
    cont_total = cont_face + cont_hi + cont_space + cont
    if cont_total != 0:  # p2
        porcentaje = (cont_pr * 100) / cont_total
        print("porcentaje de personas que utilizan alguna de las tres redes principales es: ", porcentaje)
    if not(band):  # p3
        print(f'{nombre_primero_hi} es el primer usuario procesado que usa hi5 y su edad es {edad_primer}')
    if cont_face >= cont_hi and cont_face >= cont_space:  # p4
        print("la red social mas rentable para invertir es facebook")
    elif cont_space >= cont_hi and cont_space >= cont_face:
        print("la red social mas rentable para invertir es my space")
    elif cont_hi >= cont_face and cont_hi >= cont_space:
        print("la red social mas rentable para invertir es hi5")