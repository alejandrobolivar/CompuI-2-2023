'''
La ley de Coulomb dice: “La magnitud de la Fuerza Eléctrica (Fe) entre dos cargas (q1, q2) 
puntuales es proporcional al producto de ambas cargas e inversamente proporcional 
al cuadrado de la distancia (r) entre ellas”, de aquí que la fórmula para calcular 
dicha fuerza es:𝐹𝑒=𝑘 ((𝑞1∙𝑞2))/𝑟^2 , donde k es una constante, q1 y q2 son las cargas 
en Coulomb (C) y r es la distancia en metros (m).
Considerando sus conocimientos de Física y de Programación, se le pide a Ud. que, d
ada una lista de datos con la siguiente información:

Carga 1 (C), Carga 2 (C), Distancia (m) y Medio que rodea las cargas (1=Vacío, 2=Porcelana, 3=Baquelita)
Desarrolle un Programa que procese esta información y determine:

Para cada pareja de cargas:
1)La magnitud de la Fuerza Eléctrica

Para todas las parejas de cargas:
2)Porcentaje de parejas en que la Fuerza Eléctrica es de atracción
3)Promedio de la Fuerza Eléctrica de las parejas que están en el vacío
4)Primera Fuerza Eléctrica con cargas de atracción en medio de porcelana
5)Cuál es la magnitud de la Fuerza Eléctrica donde la distancia entre las cargas es la menor y de haber varias parejas con esta misma menor distancia, entonces indique la magnitud de Fuerza Eléctrica en la primera de ellas y cuantas parejas además de ella están separadas esa misma distancia

Consideraciones:
1. La constante k depende del medio ambiente que rodea las cargas, para el Vacío, k=9000 N m²/C², para la Porcelana, k=1500 N m²/C², para la Baquelita, k=9000 N m²/C²
2. La Fuerza Eléctrica es de repulsión cuando las cargas son de la misma polaridad, es decir ambas son positivas o ambas son negativas, y la Fuerza Eléctrica es de atracción cuando las cargas son de distinta polaridad.

'declaración de variables

'Variables de entrada
ql, q2, r
medio
resp

'variables de proceso
k, cont_parejas, cont_atrac, cont_vacio, bandera, bandera2
acum_fe_vacio
menor_r

'Variables de salida
fe, porc, prom, primer_fe_vacio, fe_menor_r
cont_menor_r
'''

# Inicialización
cont_parejas = 0
bandera = True
acum_fe_vacio = 0
cont_vacio= 0
bandera2 = True
cont_menor_r = 1
cont_atrac= 0

while resp == 2:

    q1 = float(input("Valor de la Primera Carga [C]: "))
    q2 = float(input("Valor de la segunda carga [C]: "))
    r = float(input("Distancia entre las cargas [m]: "))
    medio = int(input("Tipo de medio que rodea las cargas (1=vacío, 2=porcelana, 3=baquelita): "))

    if r != 0:
        cont_parejas += 1
        if medio == 2:  # k en N m² / C²
            k = 1500
        else:
            k = 9000

        # 1) Cálculo de Fe
        fe = k * (q1 * q2) / r ^ 2
        print("1) Tienen una Fuerza eléctrica de:" , fe , "[N]")

        # 2) Datos del porcentaje
        if fe < 0: 
            cont_atrac+= 1

        # 3) Datos para el promedio
        if medio == 1:
            acum_fe_vacio += fe
            cont_vacio += 1

        # 4) Hallar primera Fe de atracción en medio=2
        if medio == 2 and fe < 0 and bandera:
            primer_fe_vacio = fe
            bandera = False

        # 5) Hallar Fe con menor distancia entre partí­culas
        if bandera2:
            menor_r = r
            fe_menor_r = fe
            bandera2 = False
        elif r < menor_r:
            menor_r = r
            fe_menor_r = fe
            cont_menor_r = 1
        elif r == menor_r:
            cont_menor_r += 1

    resp = input("¿Hay más cargas? (1=SI, 2=NO) ")

# Cálculos finales y Salida de datos
if cont_parejas > 0:
    porc = cont_atrac/ cont_parejas * 100
    print("2) El porcentaje de parejas de cargas con Fe de atracción es de: " , porc)

if cont_vacio > 0:
    prom = acum_fe_vacio / cont_vacio
    print("3) El promedio de la Fe en el vacío es de: " , prom , "[N]")
else:
    print("3) No hubo cargas en medio vací­o")

print("4) La primera Fe de atracción en porcelana tiene un valor de: " , primer_fe_vacio)

if cont_menor_r == 1:
    print("5) La Fe con menor distancia entre las cargas es de: " , fe_menor_r , "[N]")
else:
    print("5) La primera Fe con menor distancia entre las cargas es de: " , fe_menor_r , "[N] y hay " , cont_menor_r , "más con la misma distancia")