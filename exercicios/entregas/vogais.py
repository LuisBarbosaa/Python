def vogal(n):

  if(n == 'a' or n == 'e' or n == 'i' or n == 'o' or n == 'u'):
    return True
  elif(n == 'A' or n == 'E' or n == 'I' or n == 'O' or n == 'U'):
    return True
  else:
    return False

print(vogal('A'))
print(vogal('b'))
print(vogal('c'))
print(vogal('e'))