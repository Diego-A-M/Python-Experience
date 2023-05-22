#potenciação

def funcao1(base,expoente):
    resultado = base ** expoente
    return resultado

base = int(input("Digite o valor da base: "))
expoente = int(input("Digite o valor do expoente: "))

potencia = funcao1(base,expoente)

print("O resultado do cálculo é: {}".format(potencia))
