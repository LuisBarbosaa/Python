import math

valores = list(map(float, input().split()))
x1, y1, x2, y2 = valores

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

if distancia >= 10:
    print("longe")
else:
    print("perto")
