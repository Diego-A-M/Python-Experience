#calculadora
def multiplicação(x, y):
    resultado = x * y
    print("O resultado para a multiplicação é: {}".format(resultado))
    return resultado

def subtração(x, y):
    resultado = x - y
    print("O resultado para a subtração é: {}".format(resultado))
    return resultado

def adição(x, y):
    resultado = x + y
    print("O resultado da adição é {}".format(resultado))
    return resultado

def divisão(x, y):
    resultado = x / y
    print("O resultado para divisão é: {}".format(resultado))
    return resultado

def porcentagem(x, y):
    percent = y / 100
    resultado = x * percent
    print("O resultado para a porcentagem é: {}".format(resultado))
    return resultado

x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))

resolução = int(input("O que deseja fazer com os números?"
            "1 para multiplicação"
            "2 para divisão"
            "3 para adição"
            "4 para subtração"
            "5 para porcentagem"
            ))

if resolução == 1:
    resultado1 = multiplicação(x, y)
    print(resultado1)
elif resolução == 2:
    resultado1 = divisão(x, y)
    print(resultado1)
elif resolução == 3:
    resultado1 = adição(x, y)
    print(resultado1)
elif resolução == 4:
    resultado1 = subtração(x, y)
    print(resultado1)
elif resolução == 5:
    resultado1 = porcentagem(x, y)
    print(resultado1)
