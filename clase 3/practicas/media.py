auto1 = ['Mazda RX4', 21.0, 6, False, 4]
auto2 = ['Merc 240D', 24.4, 4, True, 2]
auto3 = ['Merc 280', 19.2, 6, True, 4]
auto4 = ['Valiant', 18.1, 6, True, 1]
auto5 = ['Merc 450SL', 17.3, 8, False, 3]
auto6 = ['Toyota Corolla', 33.9, 4, True, 1]


lista_concatenada=[auto1,auto2,auto3,auto4,auto5,auto6]
res = []

def promedio(x):
    return sum(x)/len(x)
def calculo_media():
    for x in range(6):
        for y in range(5):
            if (type(lista_concatenada[x][y]) is int) or (type(lista_concatenada[x][y]) is float):
                res.append(int(lista_concatenada[x][y]))
                # print(res)
                
calculo_media()            
print(promedio(res))