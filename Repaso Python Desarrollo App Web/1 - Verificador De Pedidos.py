valper = 5
valtuer = 3
valaran = 1
per = int (input ("Introduzca El Numero De Pernos: "))
tuer = int (input ("Introduzca El Numero De Tuercas: "))
aran = int (input ("Introduzca En Numero De Arandeles: "))
suma = per * valper + tuer * valtuer + aran * valaran
if per > tuer:
    print("Verificar Pedido")
    print("Costo Total: $",suma)
else:
    print("Costo Total: $",suma)