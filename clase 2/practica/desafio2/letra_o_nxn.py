ch = '*'
ch2=' '
base = ''
lateral = ''
matriz = int(input('ingrese el valor para la matriz'))

for x in range(matriz):
    if (x == 0) or (x == matriz-1):
        for j in range(matriz):
            base=base+ch
        print(base)
        base = ''
    else:
        for k in range(matriz):
            if (k == 0) or (k == matriz-1):
                lateral=lateral+ch
            else:
                lateral=lateral+ch2
            
        print(lateral)
        lateral=''