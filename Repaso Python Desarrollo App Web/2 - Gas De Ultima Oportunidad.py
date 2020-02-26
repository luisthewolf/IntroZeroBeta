tan = int (input ("Capacidad Del Tanque: "))
print("Porcentaje De Gas: ")

med = int (input ("Lectura Del Medidor: "))
mil = int (input ("Millas Por Galon: "))
gal = tan * (med/100) * mil

if gal > 200:
    print("Es Seguro Proceder!!!")
else:
    print("Consigue Gas!!!")
