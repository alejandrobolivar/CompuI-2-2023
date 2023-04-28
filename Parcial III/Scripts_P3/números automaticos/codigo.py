'''
Los numeros automaticos son aquellos nuemeros cuyos cuadrados terminan en el numero mismo. 
Los primeros numeros automaticos son 1,5,6,25,76.... 
Por definicion 0 no es numero automatico y para este ejercicio en particular, 
el numero 1 no se considera un numero automatico 
'''

def leercodigo(registro):
	linea=registro.split(',')
	numero=int(linea[0])
	return numero

def cant_dig(x):
    aux = x
    cd = 0
    while aux > 0:
        aux = aux // 10
        cd += 1
    return cd

def ult_dig(x, cd):
    aux = x
    nro = 0
    for i in range(1,cd+1):
        d = aux % 10
        aux = aux // 10
        nro = d * i + nro
    return nro

def main():
    arch1=open("numeros.txt","r")
    arch2=open("automaticos.txt","w")
    for registro in arch1:
        numero = leercodigo(registro)
        #iniciar variables
        if ult_dig(numero,cant_dig(numero)) == numero:
            arch2.write(str(numero) + "\n")
    arch1.close()
    arch2.close()
    
    # Mensaje al usuario
    input("Pulse una tecla para finalizar")

if __name__ == "__main__":
    main()