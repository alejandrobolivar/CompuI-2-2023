'''El 09 de febrero de 2010 fue decretada oficialmente la emergencia eléctrica en Venezuela, lo cual confirmó la crisis
eléctrica que se estaba viviendo en el país. Debido a esto las comunidades están evaluando su consumo eléctrico; para
ello se tiene la información de las lecturas de los medidores, de los suscriptores de una zona aleatoriamente
seleccionada, la información es la siguiente:

Número de Contrato, Tipo de Suscriptor, Lectura inicial y final del medidor en kWh

Desarrolle un programa que procese la información antes mencionada y determine e imprima:

a) Consumo eléctrico de cada suscriptor
b) Monto de la factura en Bs por cada suscriptor
c) Monto total en Bs. que deben pagar los suscriptores residenciales de alto
consumo por concepto de multa
d) Consumo eléctrico total de la zona en estudio
e) Promedio de consumo eléctrico de los suscriptores de tipo residencial
considerados de alto consumo
f) Número de Contrato del primer suscriptor de tipo residencial procesado
considerado de alto consumo
Consideraciones:
 El tipo de suscriptor se tomará como 1 para Residencial y 2 para Comercial
 El consumo eléctrico se determina como la diferencia entre las lecturas del medidor.
 Se consideran usuarios de alto consumo residencial aquellos cuyo consumo sea superior a 500 kWh.
 Cada kWh residencial cuesta Bs. X y cada kWh comercial cuesta Bs. Y.
 La multa por ser usuario residencial de alto consumo es de 50% del monto a pagar por el consumo.
 El monto de la factura será la suma del monto a pagar por el consumo eléctrico más la multa, en caso de ser usuario
residencial de alto consumo'''

# Inicialización de variables
acum_ce = 0
acum_ce_alco = 0
cont_ce_alco = 0
band = 0
resp = 1
tarifa_res = float(input('Ingrese el monto en Bs a pagar por los suscriptores residenciales: '))
tarifa_com = float(input('Ingrese el monto en Bs a pagar por los suscriptores comerciales: '))
while resp == 1:
    contrato = int(input('Ingrese el numero de contrato: '))
    linicial = float(input('Ingrese la lectura inicial del medidor: '))
    lfinal = float(input('Ingrese la lectura final del medidor: '))
    ts = int(input('Ingrese el tipo de suscriptor: \nResidencial (1) \nComercial (2) \n'))
    # Respuesta a
    ce = lfinal - linicial
    print('a) Su consumo eléctrico es: ', ce)    
    # Respuesta d
    acum_ce += ce
    # Respuesta b
    if ts == 1:  # Residencial
        monto = ce * tarifa_res

        if ce > 500:  # Alto consumo residencial
            multa = monto * 0.5
            print('Es un suscriptor de alto consumo su multa es: {multa:6.2f}')
            monto += multa
            # RESPUESTA e
            acum_ce_alco += ce
            cont_ce_alco += 1

            if band == 0:
                alco_1 = contrato
                band = 1

    else  # Comercial
        monto = ce * tarifa_com
    
    # Respuesta c

    print(f'b) Su monto a pagar es: {monto:6.2f}')

    # Respuesta f

    resp = int(input('Hay mas suscriptores? \nSI: 1 \nNO: 2'))

print(f'd) El consumo total de la zona de estudio es: {acum_ce}')
if cont_ce_alco == 0:
    print('No hubo suscriptores de alto consumo')
else:
    prom = acum_ce_alco / cont_ce_alco
    print(f'e) El promedio de consumo electrico de los suscriptores de alto consumo es: {prom:6.2f}')
print(f'f) El número de contrato del primer consumidor de alto consumo es: {alco_1}')