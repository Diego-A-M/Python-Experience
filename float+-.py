def funcao1(x, y):
    if x > y:
        maior = x
        print("O maior número é x com:", maior)
    elif y > x:
        maior = y
        print("O maior número é y com:", maior)
    else:
        print("Os números são iguais.")
        return None

    return maior

x = float(input("Informe o número de x: "))
y = float(input("Informe o número de y: "))

maior = funcao1(x, y)
print(maior)
