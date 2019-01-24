velocidad = [4, 4, 7, 7, 8, 9, 10, 10, 10,11, 11, 12, 12, 12, 12, 13, 13,13, 13, 14, 14, 14, 14, 15, 15,15, 16, 16, 17, 17, 17, 18, 18,18, 18, 19, 19, 19, 20, 20, 20,20, 20, 22, 23, 24, 24, 24, 24, 25]
distancia = [2, 10, 4, 22, 16, 10, 18, 26, 34,17, 28, 14, 20, 24, 28, 26, 34, 34,46, 26, 36, 60, 80, 20, 26, 54, 32,40, 32, 40, 50, 42, 56, 76, 84, 36,46, 68, 32, 48, 52, 56, 64, 66, 54,70, 92, 93, 120,85]
vd=[]
for i in zip(velocidad,distancia):
    vd.append(i)
def promedio(x):
    return sum(x)/len(x)
prom=promedio(velocidad)
dist=promedio(distancia)
vbp=0
vbpdsp=0
vsp=0
vspdbp=0
print('Las siguientes velocidades y distancias se encuentran bajo el promedio de velocidad')
for x in range(len(vd)):
    if (vd[x][0])<prom:
        print(vd[x])
        vbp+=1
print(f'Existen {vbp} velocidades bajo el promedio')
print('Las siguientes velocidades  se encuentran bajo el promedio y las distancias se encuentran sobre el promedio')
for x in range(len(vd)):
    if (vd[x][0])<prom and (vd[x][1])>dist:
        print(vd[x])
        vbpdsp +=1
print(f'Existen {vbpdsp} vehiculos con velocidades bajo el promedio y distancias sobre el promedio')
print('Las siguientes velocidades sobre el promedio de velocidad')
for x in range(len(vd)):
    if (vd[x][0])>prom:
        print(vd[x])
        vsp +=1
print(f'Existen {vsp} velocidades bajo el promedio')
print('Las siguientes distancias se encuentran bajo el promedio y las velocidades se encuentran sobre el promedio')
for x in range(len(vd)):
    if (vd[x][0])>prom and (vd[x][1])<dist:
        print(vd[x])
        vspdbp +=1
print(f'Existen {vspdbp} vehiculos con velocidades bajo el promedio y distancias sobre el promedio')