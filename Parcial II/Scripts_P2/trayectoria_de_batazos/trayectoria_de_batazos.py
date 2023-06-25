'''
Su profesor de física le propuso un tema de investigación de campo que consiste en
estudiar y simular las trayectorias de los batazos de los jugadores de beisbol. La idea
fundamental es crear un programa que lea de un archivo de datos de nombre
s t a d i u m . t x t , la información del stadium:
Distancia del Home al Muro por el Center Field o Largo del Campo (m) y la altura del
Muro (m)
y a continuación los datos de los batazos que se han registrado en ese stadium,
consistente de :
Bateador, Altura del Bateo (m), Velocidad de Salida (m/s) y ángulo de salida (expresado en grados)
Elabore una aplicación de consola en VB2010 que lea la información del stadium y de cada uno de los batazos en ese
stadium de los archivos indicados y determine e imprima para cada batazo en el archivo resultados.txt:
Bateador, Distancia Horizontal máxima de alcance (m), altura del batazo (m) y Situación del bateo
Además para todos los batazos, imprima por pantalla:
1. Porcentaje de Batazos que pegan en el muro
2. Bateador, Velocidad y ángulo de salida del jonrón más largo
Consideraciones:
 Distancia Horizontal máxima de alcance (m), se calcula según la siguiente fórmula:


donde V0 es la Velocidad de Salida y alfa es el ángulo de salida expresado en radianes
 Altura del Batazo (m), se calcula según la siguiente la fórmula:

donde y0 es la altura del bateo, V0 es la velocidad de salida,
alfa es el angulo de salida expresado en radianes y x es el largo del campo.

La Situación del Bateo será :
1. Está dentro del cuadro ( sí Xmax <= 36.88)
2. Cae en los outfielders (detrás de segunda base, delante del muro)
(Si (36.88 < Xmax < Largo del Campo) ó (Xmax > Largo Campo y Altura del Batazo <= Altura del Muro))
3. Jonrón, la sacó del parque (Si Xmax > Largo Campo y Altura del Batazo > Altura del Muro)
 PI radianes = 180°
 g=9.81 m/s (aceleración de la gravedad terrestre)

'''