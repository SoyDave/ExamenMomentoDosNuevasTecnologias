dict = {}
contar_frase = input("Escriba una frase o texto: ")
palabras=contar_frase.split(" ")
for palabra in palabras:
	if palabra in dict:
		dict[palabra]+=1
	else:
		dict[palabra]=1	

for campo,valor in dict.items():
	print ("En el texto encontramos la palabra <<",campo,">>","en",valor,"ocaciones")