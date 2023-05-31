def informações(x, y):
    nome = y
    ano = 2023
    id = ano - x

    if id < 65:
        Arisco = False
    elif id > 65:
        Arisco = True

    texto = ("""
    ------------------------------------
    Nome: {}
    Idade: {}
    Oferece Risco?: {}
    ------------------------------------
    """.format(nome, id, Arisco))

    if id > 65:
        print("""
        --------------------------------------------------------------------------------------
        O paciente {}, tem {} anos, sendo movido para a área de risco.
        --------------------------------------------------------------------------------------""".format(nome,id))
        
    if (id < 65):
        print("""
        --------------------------------------------------------------------------------------
        O paciente {}, tem {} anos. Deve ser translocado para a área fora de risco.
        --------------------------------------------------------------------------------------""".format(nome,id))

    risco = open('./informações pacientes/pacientes.txt', 'a')
    risco.write(texto)

name = input("Qual o nome do paciente?: ")
idd = int(input("Qual ano ele nasceu?: "))

if __name__ == '__main__':
    informações(idd,name)


