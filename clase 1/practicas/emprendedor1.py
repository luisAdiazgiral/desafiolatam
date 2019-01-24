import sys 
print('Bienvenido al programa de calculo de rentabilidad')

usuarios = (float(sys.argv[1]))
valor = (float(sys.argv[2]))
gastos= (float(sys.argv[3]))
utilidad=((usuarios*valor)-gastos)
print('La utilidad neta es: ', utilidad)
if (utilidad>0):
    impuesto=(float(utilidad))*.35
    print('El impuesto a pagar es: ',impuesto)
    print('La utilidad final (total menos los impuestos) es : ', utilidad - impuesto)
    print('')
    print('El software es rentable')
if (utilidad<0):
    print('La utilidad total es: ', utilidad)
    print('')
    print('El software NO es rentable')