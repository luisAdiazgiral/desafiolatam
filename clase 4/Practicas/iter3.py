#iter3.py
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
diccio={}
dicc={}
def filter(dicc,compara):
    for meses, valores in dicc.items():
        if valores > compara:
            diccio[meses]=valores

compara = int(input('ingrese el valor para crear el diccionadio: \n'))
filter(ventas,compara)
print(diccio)