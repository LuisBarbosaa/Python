n = int(input("Digite um numero inteiro: \n"))

soma = 0

while(n > 0):
  soma += n % 10
  n //= 10

print(f"{soma}")