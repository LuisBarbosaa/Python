def soma_elementos(lista):
  soma = 0
  for x in lista:
    soma = soma + x

  return soma

lista = [1, 2, 3, 4, 5]

resp = soma_elementos(lista)

print(resp)