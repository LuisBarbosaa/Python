def computador_escolhe_jogada(n, m):
    if n % (m + 1) == 0:
        return m  # Retira o máximo possível
    else:
        return n % (m + 1)  # Deixa múltiplo de (m + 1)

def usuario_escolhe_jogada(n, m):
    while True:
        jogada = int(input(f"Quantas peças você vai retirar? (1 a {m}): "))
        if 1 <= jogada <= min(m, n):
            return jogada
        else:
            print(f"Jogada inválida! Você deve retirar entre 1 e {min(m, n)}.")

def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    
    if n % (m + 1) == 0:
        print("Você começa!")
        jogador_começa = True
    else:
        print("Computador começa!")
        jogador_começa = False
    
    while n > 0:
        if jogador_começa:
            jogada_usuario = usuario_escolhe_jogada(n, m)
            n -= jogada_usuario
            print(f"Você retirou {jogada_usuario} peça(s). Restam {n} peça(s).")
            if n == 0:
                print("Você ganhou!")
                return
        else:
            jogada_computador = computador_escolhe_jogada(n, m)
            n -= jogada_computador
            print(f"O computador retirou {jogada_computador} peça(s). Restam {n} peça(s).")
            if n == 0:
                print("O computador ganhou!")
                return
        
        jogador_começa = not jogador_começa  # Alterna o jogador

def campeonato():
    placar_usuario = 0
    placar_computador = 0
    
    for i in range(3):
        print(f"\n--- Partida {i + 1} ---")
        partida()
        if n == 0 and jogador_começa:  # Se o usuário ganhou
            placar_usuario += 1
        elif n == 0 and not jogador_começa:  # Se o computador ganhou
            placar_computador += 1
            
    print(f"\nPlacar: Você {placar_usuario} X {placar_computador} Computador")

if __name__ == "__main__":
    opcao = int(input("Escolha: 1 - Partida  |  2 - Campeonato: "))
    if opcao == 1:
        partida()
    elif opcao == 2:
        campeonato()