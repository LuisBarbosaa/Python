def eh_hipotenusa(h):
    for i in range(1, h):
        for j in range(1, h):
            if i**2 + j**2 == h**2:
                return True
    return False

def soma_hipotenusas(n):
    soma = 0
    for num in range(1, n + 1):
        if eh_hipotenusa(num):
            soma += num
    return soma

print(soma_hipotenusas(25)) 