texto = input("ingrese un texto: ")
def contadorCaracteres(texto):
    caracteres = texto.lower().replace(" ", "")
    cantidad = dict()

    for caracter in caracteres:
        if caracter in cantidad:
            cantidad[caracter] += 1
        else:
            cantidad[caracter] = 1

    print("los caracteres se repiten ")
    for key, value in cantidad.items():
        print(key, ' <-> ', value)

print(contadorCaracteres(texto))