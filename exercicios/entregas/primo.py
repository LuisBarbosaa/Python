num = int(input("Digite um numero inteiro: \n"))

if(num <= 1):
  print("Não primo")
else:
  divisor = 2
  primo = True
  while(divisor * divisor <= num):
    if(num % divisor == 0):
      primo = False
      break
    divisor += 1

if(primo):
  print("Primo")
else:
  print("Não primo")