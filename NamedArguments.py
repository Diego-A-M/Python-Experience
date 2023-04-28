#Argumentos nomeados

def imprimir_carro(modelo, ano, qualidade):
    print("Modelo do carro: ", modelo)
    print("Ano do carro: ", ano)
    print("Qualidade do carro: ", qualidade)

modelo = input("Digite o modelo do carro" )
ano = input("Digite o ano do carro ")
qualidade = input("Qual a qualidade do veículo? ")

imprimir_carro(modelo=modelo, ano=ano, qualidade=qualidade)

#Neste exemplo eu utilizei um questionário sobre carros.
