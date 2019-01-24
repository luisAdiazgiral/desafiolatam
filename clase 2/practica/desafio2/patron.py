def patron1(cont):
    c1='*'
    c2='.'
    frase=''
    if cont%2==0:
        cont=cont-1
    for x in range(cont):
        if x%2 ==0:
            frase = frase + c1
        else:
            frase = frase + c2
    print(frase)
def patron2(cont):
    c1='**'
    c2='..'
    frase=''
    if cont%2==0:
        cont=cont-1
    for x in range(cont):
        if x%2 ==0:
            frase = frase + c1
        else:
            frase = frase + c2
    print(frase)
def patron3(cont):
    c1='1'
    c2='2'
    frase=''
    if cont%2!=0:
        cont=cont-1
    for x in range(cont):
        if x%2 ==0:
            frase = frase + c1
        else:
            frase = frase + c2
    print(frase)
def patron4(cont):
    c1='12'
    c2='3'
    frase=''
    if cont%2!=0:
        cont=cont-1
    for x in range(cont):
        if x%2 ==0:
            frase = frase + c1
        else:
            frase = frase + c2
    print(frase)
veces=int(input('cuantas veces desea repetir el patron?'))
patron1(veces)
patron2(veces)
patron3(veces)
patron4(veces)