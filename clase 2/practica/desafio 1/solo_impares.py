numero = int(input('Ingrese un numero para mostrar los impares:  '))
numero = numero * 2
for x in range(numero):
    if x%2 !=0:
        print(x)