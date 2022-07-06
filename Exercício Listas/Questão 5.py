pontos = 0
perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]

for pergunta in perguntas:
   print(pergunta)
   resposta = input("Responda sim ou nao: ")

   if resposta == "sim":
       pontos +=1

if pontos == 2:
   print("Esta pessoa é suspeita.")
elif 3 <= pontos < 5:
   print("Esta pessoa é cúmplice!")
elif pontos == 5:
   print("Esta pessoa é o assassino!")
else:
   print("Esta pessoa é inocente.")