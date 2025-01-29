lista = []

num = int(input("Digite um número (0 para sair): "))
while num != 0:
    lista.append(num)
    num = int(input("Digite um número (0 para sair): "))

lista.reverse()

for numero in lista:
    print(numero)