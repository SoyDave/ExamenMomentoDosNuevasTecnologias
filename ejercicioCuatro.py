nombres = input("Ingrese nombres, 0 para salir: ")

lista_nombres = []

while nombres != "0":
    lista_nombres.append(nombres)
    nombres = input("Ingrese nombres, 0 para salir: ")


for nombre in lista_nombres:
    if nombre[0] == 'c' or nombre[0] == 'C':
        print("el nombre", nombre, "inicia con c/C")
    else:
        print("el nombre", nombre, " no inicia con c/C")