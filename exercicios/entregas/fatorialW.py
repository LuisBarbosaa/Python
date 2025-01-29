n = int(input("Digite o valor de n:\n"))

fat = 1
i = n

while (i > 0):
  if (n == 0):
    fat = 1
  else:
   fat *= i
   i = i - 1

print(f"{fat}")