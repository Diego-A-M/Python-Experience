#função com parametros

def funct(parametro):
    print("Olá! ", parametro)

nome1 = input("Qual seu nome? ")
funct(nome1)

#Explicito é melhor do que implicito... Então:

def funct2(nome, sobrenome):
    print("Olá!", nome, sobrenome,"!")

nome = input("Qual seu nome? ")
sobrenome = input("E seu sobrenome? ")
funct2(nome, sobrenome)

#Parametros basicamente servem para resgatar dados fora do bloco de código interno de uma função, para que sejam colocados dentro da mesma.
