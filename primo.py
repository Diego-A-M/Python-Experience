#Numeros primos

print(30 * "-")

numero =  int(input("Insira um número para descobrir se é primo ou não: "))

if numero > 1:
    for x in range(2,numero):
        if(numero % x ) == 0:
            print("Esse não é primo")
            break
    else:
        print("Esse número é primo")
else:
    ("Esse número não é primo: Número menor ou igual a 1")
