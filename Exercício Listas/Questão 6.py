nome = []
kms = []
km = 0
for c in range(5):
    print(f"\nVeiculo {c + 1}")
    nome.append(input("Nome: "))
    km = float(input("KM por litro: "))
    kms.append(km)

print("\nRelatorio Final")
menor = 0
nme = ' '
for c,d in enumerate(nome):
    print(f"{c + 1}   -   {d}   -   {kms[c]}   -   {1000/kms[c]:.2f} litros   -   {1000/kms[c]*2.25:.2f} reais")
    if kms[c] > menor:
        menor = kms[c]
        nme = nome[c]

print(f"\nO menor consumo é do {nme}\n") 