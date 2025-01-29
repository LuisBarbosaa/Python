import math

x1 = int(input("Digite o valor da primeira cordenada x: \n"))
y1 = int(input("Digite o vaalor da primeira cordenada y: \n"))
x2 = int(input("Digite o valor da segunda cordenada x: \n"))
y2 = int(input("Digite o vaalor da segunda cordenada y: \n"))

distancia = (x1 - x2)**2 + (y1 - y2)**2
distancia = math.sqrt(distancia)

if(distancia >= 10):
  print(f"A distancia é {distancia}, sendo assim: Longe")
else:
  print(f"A distancia é {distancia}, sendo assim: Perto")