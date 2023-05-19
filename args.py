def imprimir_carro(nomeCarro, n_placa, potencia=None, *args):
    print("----------------")
    print("Nome do carro: ", nomeCarro)
    print("Número da placa: ", n_placa)
    if potencia != None:
        print("Potência do carro: ", potencia)


nomeCarro = input("Qual o nome do carro? ")
n_placa = input("Qual a placa? ")
potencia = input("Qual a potência? ")

imprimir_carro(nomeCarro, n_placa, potencia)

def imprimir_nomes(*nomes):
    print(nomes)

lista = ["Diego", "Augusto", "Moraes"]
imprimir_nomes(*lista)
