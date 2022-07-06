lista1 = []
lista2 = []
lista3 = []
lista4 = []

print("Primeira lista")
for i in range(10):
    lista1.append(int(input(f'Digite o valor do {i+1}° elemento: ')))

print("Segunda lista")
for i in range(10):
    lista2.append(int(input(f'Digite o valor do {i+1}° elemento: ')))

print("Terceira lista")
for i in range(10):
    lista3.append(int(input(f'Digite o valor do {i+1}° elemento: ')))

for i in range(10):
    lista4.append(lista1[i])
    lista4.append(lista2[i])
    lista4.append(lista3[i])

print(f'A quarta lista: {lista4}')