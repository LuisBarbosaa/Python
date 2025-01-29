def n_primos(n):
    def eh_primo(x):
        if x < 2:
            return False
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True
    
    count = 0
    for num in range(2, n + 1):
        if eh_primo(num):
            count += 1
    return count

print(n_primos(2)) 
print(n_primos(4))  
print(n_primos(121)) 