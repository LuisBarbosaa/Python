def maior_elemento(lista):
  maiorEle = -99999
  for x in lista:
    if(x > maiorEle):
      maiorEle = x

  return maiorEle


lista = [324, 45, 2, 45, 567, 432, 345]

maiorEle = maior_elemento(lista)

print(f"O maior elemento da lista: {lista} é --> {maiorEle}")