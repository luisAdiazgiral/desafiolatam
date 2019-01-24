#busqueda.py
import sys
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
dato=sys.argv[1:]
compara2=0
valores2=0
for compara in dato:

	for meses, valores in ventas.items():
		if valores == int(compara):
			print(meses,"\n")
			
	if valores != int(compara):
		print("no encontrado \n")
	