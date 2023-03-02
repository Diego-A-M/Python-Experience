#Exercício 2

nome = input("Informe seu nome: ")
idade = input("Informe sua idade: ")

if int(idade) >= 5 and int(idade) <= 7:
    print("Olá {}, você competirá na liga Infantil A".format(nome))
elif int(idade) >= 8 and int(idade) <= 10:
    print("Olá {}, você competirá na liga Infantil B".format(nome))
elif int(idade) >= 11 and int(idade) <= 13:
    print("Olá {}, você competirá na liga Juvenil A".format(nome))
elif int(idade) >= 14 and int(idade) <= 17:
    print("Olá {}, você competirá na liga Juvenil B".format(nome))
