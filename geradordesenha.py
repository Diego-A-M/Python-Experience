#Gerador de senhas
""


""

chave = input("Digite a base de sua senha: ")

senha = ""

Security = chave
Secur1ty = senha


for letra in chave:
    if letra in "Aa": senha = senha + "10"
    elif letra in "Bb": senha = senha + "11"
    elif letra in "Cc": senha = senha + "12"
    elif letra in "Dd": senha = senha + "13"
    elif letra in "Ee": senha = senha + "14"
    elif letra in "Ff": senha = senha + "15"
    elif letra in "Rr": senha = senha + "#"
    elif letra in "Ss": senha = senha + "$"
    elif letra in "Tt": senha = senha + "7"
    else: senha = senha + letra

print(senha)
