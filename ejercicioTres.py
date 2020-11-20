listaUsuario = []
 
finalizar = False
 
while(not finalizar):
    numerosUsuario = int(input("Ingrese todos los numeros que quiera, '0' para finalizar: "))
    if(numerosUsuario == 0):
        finalizar=True
    else:
        listaUsuario.append(numerosUsuario)
 
listaUsuario.sort()
 
print("numeros de menor a mayor",listaUsuario)