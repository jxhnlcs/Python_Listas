lista1 = []
lista2 = []
lista3 = []

print("Primeira lista")
for i in range(10):
    lista1.append(int(input(f'Digite o valor do {i+1}° elemento: ')))

print("Segunda lista")
for i in range(10):
    lista2.append(int(input(f'Digite o valor do {i+1}° elemento: ')))

for i in range(10):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

print(f'A terceira lista: {lista3}')