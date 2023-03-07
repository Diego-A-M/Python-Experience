import math

x = 9
y = 8
soma = x + y
multiplicacao = x * y
divisao = x / y

print("O resultado da adição é {}".format(soma))
print("O resultado da multiplicação é {}".format(multiplicacao))
print("O resultado da divisão é {}\n\n".format(divisao))


#Exibindo utilizando o conceito de F-strings que foram introduzidas no Python 3.6 através da PEP 498.
print(f"O resultado da adição é {soma}")
print(f"O resultado da multiplicação é {multiplicacao}")
print(f"O resultado da divisão é {divisao:.2f}") # .2f é uma forma de formatar para que o valor aparece com 2 casas decimais
