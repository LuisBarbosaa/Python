def fizzbuzz(n):
  if(n % 3 == 0 and n % 5 != 0):
    return 'Fizz'
  elif(n % 5 == 0 and n % 3 != 0):
    return 'Buzz'
  elif(n % 3 == 0 and n % 5 == 0):
    return 'FizzBuzz'
  else:
    return n

print(fizzbuzz(3))
print(fizzbuzz(10))
print(fizzbuzz(15))
print(fizzbuzz(4))