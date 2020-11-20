def indiceMasaCorporal(estatura, peso):
    return peso / estatura**2

peso = float(input("¿Cuanto pesas en KG? "))
estatura = float(input("¿Cuanto mides en M? "))

indiceMasa = indiceMasaCorporal(estatura, peso)

if indiceMasa < float(18.5):
    print("su peso es", indiceMasa, "Peso insuficiente")
elif indiceMasa > float(18.5) and indiceMasa < float(24.9):
    print("su peso es", indiceMasa, "Normopeso")
elif indiceMasa > float(25) and indiceMasa < float(26.9):
    print("su peso es", indiceMasa, "Sobrepeso grado I")
elif indiceMasa > float(27) and indiceMasa < float(29.9):
    print("su peso es", indiceMasa, "Sobrepeso grado II (preobesidad)")
elif indiceMasa > float(30) and indiceMasa < float(34.9):
    print("su peso es", indiceMasa, "Obesidad de tipo I")
elif indiceMasa > float(35) and indiceMasa < float(39.9):
    print("su peso es", indiceMasa, "Obesidad de tipo II")
elif indiceMasa > float(40) and indiceMasa < float(49.9):
    print("su peso es", indiceMasa, "Obesidad de tipo III (mórbida)")
else: 
    print("su peso es", indiceMasa, "Obesidad de tipo IV (extrema)")