import random

lista1 = random.sample(range(50), 30)
lista2 = random.sample(range(50), 20)
vet = lista1 + lista2
vet.sort()

repetidos = []
for i in vet:
    if (vet.count(i) > 1):
        repetidos.append(i)

print(repetidos)