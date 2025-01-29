largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

for i in range(altura):
  if i == 0 or i == altura - 1:
    print('#' * largura)
  else:
    if largura > 1:
      print('#' + ' ' * (largura - 2) + '#')
    else:
      print('#')