#piedra papel tijera
import sys
from random import randrange, choice
juego_usuario=(sys.argv[1])
error=0
if juego_usuario == ("tijeras"):
	jusr = 1
elif juego_usuario== "piedra":
	jusr = 2
elif juego_usuario== "papel":
	jusr = 3
else:	
	
	error=1
if error == 1:
	print ("debe elegir solo piedra, papel o tijeras")
else: 
	juego_pc = (choice(["tijeras", "piedra", "papel"]))
	if juego_pc == ("tijeras"):
		jpc = 1
	elif juego_pc== "piedra":
		jpc = 2
	else: 
		jpc = 3

	if ((jusr==3) and (jpc==3)):
		print (f'El usuario jugo {juego_usuario}')
		print  (f'El equipo jugo  {juego_pc}')
		print("empate")
	elif ((jusr==3) and (jpc==2)):
		print (f'El usuario jugo {juego_usuario}')
		print  (f'El equipo jugo  {juego_pc}')
		print("Gana el jugador")
	elif ((jusr==3) and (jpc==1)):
		print (f'El usuario jugo {juego_usuario}')
		print  (f'El equipo jugo  {juego_pc}')
		print("Gana el computador")
	if ((jusr==2) and (jpc==2)):
		print (f'El usuario jugo {juego_usuario}')
		print  (f'El equipo jugo  {juego_pc}')
		print("empate")
	elif ((jusr==2) and (jpc==1)):
		print (f'El usuario jugo {juego_usuario}')
		print  (f'El equipo jugo  {juego_pc}')
		print("Gana el jugador")
	elif ((jusr==2) and (jpc==3)):
		print (f'El usuario jugo {juego_usuario}')
		print  (f'El equipo jugo  {juego_pc}')
		print("Gana el computador")
	if ((jusr==1) and (jpc==1)):
		print (f'El usuario jugo {juego_usuario}')
		print  (f'El equipo jugo  {juego_pc}')
		print("empate")
	elif ((jusr == 1) and (jpc== 3)):
		print (f'El usuario jugo {juego_usuario}')
		print  (f'El equipo jugo  {juego_pc}')
		print("Gana el jugador")
	elif((jusr == 1) and (jpc == 2)):
		print (f'El usuario jugo {juego_usuario}')
		print  (f'El equipo jugo  {juego_pc}')
		print("Gana el computador")
	else:
		print("")
	# print (f'El usuario jugo {juego_usuario}')

	# print  (f'El equipo jugo  {juego_pc}')