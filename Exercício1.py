#Exercícios 2 Lista da Danki Code

#Exercício 1 - Implemente um programa que receba a idade de uma pessoa e imprima a mensagem de acordo com os critérios: Menor de 16 anos = Menor; Entre 16 e 18 anos = Emancipado; Maior de 18 anos = Maior.


nome = input("Como você se chama? ")
idade = input("Qual sua idade? ")

if int(idade) > 18:
    print("Seu nome é {} e você é maior de idade, com {} anos.".format(nome,idade))
elif int(idade) < 16:
    print("Seu nome é {} e você é menor de idade, com {} anos.".format(nome,idade))
elif int(idade) >= 16 & int(idade) == 18:
    print("Seu nome é {} e você é Emancipado, com {} anos.".format(nome,idade))