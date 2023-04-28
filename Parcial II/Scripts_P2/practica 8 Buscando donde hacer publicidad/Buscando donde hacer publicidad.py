'''Con la intención de hacer la web más social se han creado múltiples aplicaciones o sitios en Internet que
permiten compartir información y establecer comunicación entre grupos de personas, estos sitios
son denominados REDES SOCIALES. Una empresa de publicidad cuyo lema es “las empresas que invierten
en publicidad, son las empresas que permanecen en la mente de las personas”, quiere evaluar la posibilidad de
colocar publicidad en alguna de las tres redes sociales que considera de mayor uso o más
comunes. Para ello se realiza una encuesta a un conjunto W de personas a quienes se les solicita
suministren la siguiente información: 
NOMBRE, GÉNERO, EDAD Y RED SOCIAL MÁS UTILIZADA

Desarrolle un programa que procese la información, almacenada en un archivo de nombre REDES.TXT y
genere dos archivos de nombre USAREDSOCIAL.TXT y NOLASENCUESTADAS.TXT, con los nombres de los
usuarios que usan alguna de las tres redes sociales consideradas en el estudio o los que no usan
ninguna de las redes sociales consideradas en el
estudio respectivamente, además...

determine e imprima por pantalla:

✓ Cantidad de personas que utilizan cada uno de las tres principales redes sociales
considerados en la encuesta
✓ Porcentaje de personas que utilizan alguna de las tres principales redes sociales
considerados en la encuesta
✓ Nombre y edad del primer usuario procesado que usa hi5
✓ En cuál de las tres redes sociales sería más rentable invertir en publicidad.

Consideraciones:
o El género se tomará como 1 =Femenino y 2 = Másculino
o Los valores para tipo de red social más utilizada son 1 =Facebook, 2 =Myspace, 3=Hi5 y
4=Ninguno u otro
o Mientras más usuarios usen una red social, esta se considera más rentable para hacer
publicidad

Actividades a Desarrollar:
1. Identifique los datos de entrada y salida, colocándolos en esta tabla con el tipo de
dato

'''

#inicializacion
linea = 1
cont1 = 0
cont2 = 0
cont3= 0
band = 0

arch1 = open('redes.txt','r')
arch2 = open('usaredsocial.txt','w')
arch3 = open('nolasencuestadas.txt','w')

contenido = arch1.readlines()

w = int(contenido[0])

for i in range(w):

    lista = contenido[linea].split(',')
    linea += 1

    nombre = str(lista[0])
    genero =str(lista[1])
    edad = int(lista[2])
    red = int(lista[3])

    if red == 4:
        arch3.write(str(nombre) + '\n')

    else:
        arch2.write(str(nombre)  + '\n')

        if red == 1:
            cont1 += 1
            f = 'facebook'
        elif red == 2:
            cont2 += 1
            m = 'myspace'
        else:
            cont3 += 1
            h = 'Hi5'

            if band == 0:
                nombre_primer = nombre
                edad_primer = edad
                band = 1

por = (cont2 + cont3 + cont1) / w * 100

print(' %d personas usan %s' % (cont1,f))
print(' %d personas usan %s' % (cont2,m))
print(' %d personas usan %s' % (cont3,h))

print('el %.2f' % por, '% de personas usan una de las tres principales redes sociales' )

print('la primera persona encuestada que usa Hi5 es %s con %d años de edad' %(nombre_primer, edad_primer))

if cont1 > cont2 and cont1 > cont3:
    print('la red social mas usada es ', f)
elif cont2 > cont1 and cont2 > cont3:
    print('la red social mas usada es ', m)
else:
    print('la red social mas usada es ', m)

arch1.close()
arch2.close()
arch3.close()