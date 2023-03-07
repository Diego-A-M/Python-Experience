#Verificação de sinal numérico

numero = int(input("Digite um número: "))

if numero > 0:
    print("O {numero} é positivo.")
elif numero < 0:
    print("O {numero} é negativo.")
elif numero == 0:
    print("O {numero} é igual a zero.")
    
#Pode-se usar um else na ultima alternativa, porém eu prefiro usar um elif e deixar mais exato o que eu quero que o programa faça
