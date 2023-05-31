"""
Paradigma orientado a objetos
"""

def Registrar(nome, idade, cpf, email):
    paciente = {'nome': nome, 'idade': idade, 'cpf': cpf, 'email': email}
    return paciente
"""
Classe
Objeto
Construtor
"""

class paciente:
    def __init__(self):
        print("Eu sou o construtor.")
        pass
