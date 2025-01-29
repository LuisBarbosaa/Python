numero = input("Digite um número inteiro: ")

possui_adjacente_igual = False
for i in range(len(numero) - 1):
    if numero[i] == numero[i + 1]:
        possui_adjacente_igual = True
        break

if possui_adjacente_igual:
    print("sim")
else:
    print("não")