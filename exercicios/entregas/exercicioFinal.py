# Tamanho médio de palavra: Média simples do número de caracteres por palavra. --> NC / P
# Relação Type-Token: Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras --> PD / TP
# Razão Hapax Legomana: Número de palavras utilizadas uma única vez dividido pelo número total de palavras -->  PU1 / TP
# Tamanho médio de sentença: Média simples do número de caracteres por sentença. --> NC / S
# Complexidade de sentença: Média simples do número de frases por sentença. --> NF / S
# Tamanho médio de frase: Média simples do número de caracteres por frase --> NC / F

import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    soma = 0
    for i in range(6):
        soma += abs(as_a[i] - as_b[i])
    return soma / 6


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    sentencas = separa_sentencas(texto)
    frases = []
    palavras = []
    
    for sentenca in sentencas:
        frases.extend(separa_frases(sentenca))
    
    for frase in frases:
        palavras.extend(separa_palavras(frase))

    tamanho_palavras = sum(len(palavra) for palavra in palavras)
    wal = tamanho_palavras / len(palavras)
    
    ttr = n_palavras_diferentes(palavras) / len(palavras)
    
    hlr = n_palavras_unicas(palavras) / len(palavras)
    
    tamanho_sentencas = sum(len(sentenca) for sentenca in sentencas)
    sal = tamanho_sentencas / len(sentencas)
    
    sac = len(frases) / len(sentencas)
    
    tamanho_frases = sum(len(frase) for frase in frases)
    pal = tamanho_frases / len(frases)
    
    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    menor_similaridade = float('inf')
    texto_mais_similar = 0
    
    for i, texto in enumerate(textos):
        assinatura_texto = calcula_assinatura(texto)
        similaridade = compara_assinatura(assinatura_texto, ass_cp)
        
        if similaridade < menor_similaridade:
            menor_similaridade = similaridade
            texto_mais_similar = i + 1
    
    return texto_mais_similar

def main():
    assinatura_cp = le_assinatura()
    textos = le_textos()
    
    texto_infectado = avalia_textos(textos, assinatura_cp)
    print(f"O texto {texto_infectado} está mais provavelmente infectado por COH-PIAH.")

main()