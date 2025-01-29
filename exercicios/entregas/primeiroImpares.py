n = int(input("Digite o valor de n: \n"))

contagem = 0
numero = 1

while (contagem < n):
  if(numero % 2 != 0):
    print(numero)
    contagem = contagem + 1
  numero = numero + 1