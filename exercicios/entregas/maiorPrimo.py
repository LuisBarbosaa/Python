def eh_primo(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def maior_primo(n):
    while n >= 2:
        if eh_primo(n):
            return n
        n -= 1

print(maior_primo(100))
print(maior_primo(7))