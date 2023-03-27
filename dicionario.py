#O Que eu aprendi com dicionários em Python

#Dicionários em python são variáveis que possui uma coleção não ordenada, são mutáveis e não permitem valores duplos.

dicio = {"nome": "Gustavo", "Idade": 9, "Nacionalidade": "Brasileiro."}

print(dicio) #Printar o dicionário
print(dicio.values()) #Printar apenas os valores
print(dicio.keys()) #Printar apenas as chaves
print(dicio.get("nome")) #printa um valor especifico, especificando assim sua chave no comando.
if "Idade" in dicio:
    print("A Chave idade existe")


x = input("Digite o nome:")
while not x.isalpha():
    print("Valor inválido, digite apenas letras.")
    x = input("Digite o nome:")

y = input("Digite a idade: ")
while not y.isnumeric():
    print("Valor inválido, digite apenas números.")
    y = input("Digite a idade: ")

dicio2 = {"nome2": x, "idade": y}
print(dicio2)

print("O dono {} tem {} Anos e é responsável por esta nota.".format(dicio2.get("nome2"),dicio2.get("idade")))
