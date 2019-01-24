base = '*   *'
base2= ' * * '
base3 = '  *  '
for x in range(5):
    if (x == 0) or (x == 4):
        print(base)
    elif (x == 1) or (x == 3):
        print(base2)
    else:
        print(base3)
