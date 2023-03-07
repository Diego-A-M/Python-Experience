#Código para adivinhar um número.

palpite = 0
numero = 9

print("Adivinhe qual o número correto: ")
palpite = int(input())

while palpite != numero:
    print("Errou.")
    print("Tente novamente")
    palpite = int(input())

if palpite == numero:
    print("Parabéns! Você acertou!")
