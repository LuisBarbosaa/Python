def maximo(a, b, c):
  if(a > b and a > c):
    return a
  elif(b > a and b > c):
    return b
  else:
    return c

print(maximo(30, 14, 10))
print(maximo(0, -1, -1))