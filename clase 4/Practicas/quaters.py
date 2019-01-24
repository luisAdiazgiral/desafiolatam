#quaters
ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000, 
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000, }
valores=[]
quaters={"Q1","Q2","Q3","Q4"}
valores=list(ventas.values())
for x in valores:
    if x<2:
        q1 += x
        print(q1)
    elif x>2 and x<5:
        q2 += x
print(quaters)
