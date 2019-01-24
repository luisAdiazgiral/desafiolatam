import string
def mostrar(veces):
    print(string.ascii_lowercase[:veces])
veces = int(input('Igrese la cantidad de letras a mostrar'))
mostrar(veces)