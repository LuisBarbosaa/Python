import math

a = float(input())
b = float(input())
c = float(input())

delta = b**2 - 4*a*c

if delta < 0:
    print("esta equação não possui raízes reais")
elif delta == 0:
    raiz = -b / (2*a)
    print(f"a raiz dupla desta equação é {raiz}")
else:
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    raiz2 = (-b - math.sqrt(delta)) / (2*a)
    if raiz1 > raiz2:
        raiz1, raiz2 = raiz2, raiz1
    print(f"as raízes da equação são {raiz1} e {raiz2}")
