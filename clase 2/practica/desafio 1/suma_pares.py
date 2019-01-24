numero = int(input('Ingrese un numero para sumar los pares:  '))
numero = numero * 2
suma = 0
for x in range(numero):
    if x%2 ==0:
        acum = x + 2
        suma += acum
print(f'el resultado de la suma es : {suma}')