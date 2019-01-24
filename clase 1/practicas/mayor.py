import sys
num1 = float(sys.argv[1])
num2 = float(sys.argv[2])
num3 = float(sys.argv[3])
if (num1 > num2):
	mayor = num1
else:
	mayor=num2
if (mayor < num3):
	mayor=num3
print(mayor)

