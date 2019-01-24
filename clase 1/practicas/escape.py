import sys
import math
gravedad = (float(sys.argv[1]))
radio = (float(sys.argv[2]))
ve = math.sqrt((2*radio*1000*gravedad))
print('La velocidad de escape es de:  ',ve,' km/h')