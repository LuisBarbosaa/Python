def remove_repetidos(lista):
    nova_lista = []
    for ele in lista:
        if ele not in nova_lista:  # Verifica se o elemento já está na nova lista
            nova_lista.append(ele)

    nova_lista.sort()

    return nova_lista

lista = [2, 4, 2, 2, 3, 3, 1]

resp = remove_repetidos(lista)

print(resp)