c1='*'
c2=' '
base = ''
lateral = ''
aux=4
b=0
for k in range(5):
    base=base+c1
for x in range(5):
    if (x == 0) or (x == 4):
        print(base)
    else:
        for x in range(1):
            for x in range(aux):
                lateral=lateral+c2
            lateral=lateral+c1
            print(lateral)
            aux -=1
            lateral=''
