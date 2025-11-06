import sys
import math

def heron(number, iterations):
    x = 1
    for n in range(1, iterations+1):
        x = (x+(number/x))/2
    return x

try:
    number = int(sys.argv[1])
    iterations = int(sys.argv[2])
except (IndexError, ValueError):
    print('usage: %s <number> <iterations>' % sys.argv[0])
else:
    print(heron(number, iterations))
