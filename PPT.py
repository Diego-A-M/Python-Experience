from random import choice
jogador_vitorias = 0
maq_vitorias = 0

def Opcao_Jogador():
    esc_jogador = input("Escolha entre pedra, papel ou tesoura")
    esc_jogador.lower()
    if esc_jogador == "pedra":
        return esc_jogador
    elif esc_jogador == "papel":
        return esc_jogador
    elif esc_jogador == "tesoura":
        return esc_jogador
    else:
        print("Escolha um valor válido.")
        Opcao_Jogador()

def Opcao_Maquina():
    maq_escolha = choice(["pedra", "papel", "tesoura"])
    return maq_escolha

while True:

    print("-"*30)
    esc_jogador = Opcao_Jogador()
    esc_maquina = Opcao_Maquina()
    print("-"*30)

    if(esc_jogador == "pedra") and (esc_maquina == "tesoura") \
        or (esc_jogador == "papel") and (esc_maquina == "pedra") \
            or (esc_jogador == "tesoura") and (esc_maquina == "papel"):
            print(f"O Jogador escolheu {esc_jogador}, e a máquina escolheu {esc_maquina}, Resultado: Você ganhou!")
            jogador_vitorias += 1
    if(esc_maquina == "pedra") and (esc_jogador == "tesoura") or (esc_maquina == "papel") and (esc_jogador == "pedra")\
        or (esc_maquina == "tesoura") and (esc_jogador == "papel"):
        print(f"O Jogador escolheu {esc_jogador}, e a máquina escolheu {esc_maquina}, Resultado: Você perdeu.")
        maq_vitorias += 1

    print("-" * 30)
    print(f"vitorias do jogador: {jogador_vitorias}")
    print(f"vitorias da maquina: {maq_vitorias}")
    print("-" * 30)



    esc_jogador = input("Você quer jogar novamente?")
    if esc_jogador in ["SIM", "sim", "Sim", "S", "s", "ss", "Ss", "SS"]:
        pass
    elif esc_jogador in ["NAO", "nao", "Nao", "N", "n", "nn", "Nn", "NN", "não", "Não"]:
        break
    else:
        print("Por favor, escolha corretamente.")
        break
