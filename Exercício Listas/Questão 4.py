temp = []
meses = ["Janeiro","Fevereiro","Março","Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
media = 0
acimaMedia = {}

for i in range(len(meses)):
    temp.append(int(input("Informe a Temperatura media de " + meses[i] + ":\n")))
    media += temp[i]
media = media/len(meses)

for i in range(len(meses)):
 	if(temp[i] > media):
 		acimaMedia.update({meses[i] : temp[i]})


print("Media das temperaturas :" + str(media))
print("Meses com temperaturas acima da media: "+ str(acimaMedia))
