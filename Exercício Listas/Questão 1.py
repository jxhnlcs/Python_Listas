def calcMedia(aluno):
    print(f"Notas do aluno {aluno}")

    total=0
    for i in range(0,4):
        total+=float(input(f"Digite a {i+1}ª nota: "))
    return total/4

def mostraMedia(lst):
    aprovado=0
    for i in lst:
        if i >=7:
            aprovado+=1
    print(f"As médias foram: {lst}")
    print(f"Há {aprovado} aluno(s) com média maior que 7,0")

medias= []

for i in range(0,10):

    medias.append(calcMedia(i+1))  

    print()

mostraMedia(medias)

