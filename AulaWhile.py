a = 0 #valor inicial

while a <= 5: #Enquanto A For menor igual a 5 faça:
    print(a <= 5) #Verificação para ver se é True
    print(a) #Print do valor do objeto de A
    if a == 3: #Valor desejado
        break #Break para parar o fluxo de ordens onde A ganha mais um número até atingir o 5. Obejtivo final é atingir três.
    a = a + 1

print("Resultado final de A: ", a)
print(a <= 5)