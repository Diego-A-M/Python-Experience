vetor = [10, 23, 42, 55]
print(vetor)

vetor2 = ["Gustavo", "Gabriel", "Lucas", "Fernando"]
print(vetor2)

vetor3 =["Gustavo", 11, "Gabriel", 42,"Lucas",59]
print(vetor3)

print(type(vetor3))

print(vetor3[1])

print(vetor3[1:])
print(vetor3[2:])
print(vetor3[:3])
print(vetor3[:4])
print(vetor3[1:4])

vetor2 = vetor2 + vetor3
print(vetor2)

n1 = "Curso de Python"
n2 = range(10)

print(n1)
print(n2)

lista7 = list(range(10))
print(lista7)

lista8 = list("Curso de python")
print(lista8)

elemento = 8

if elemento in lista7:
    print("Este elemento está dentro da lista")

vetor9 = ["Gato", "Cão", "Cavalo", "Urso"]
print(vetor9)

vetor9[1] = 'Cachorro'
print(vetor9)

vetor9[1::3] = "Desconhecido"
