pa = float (input ("Precio Por Libra Paquete A: "))
ma = float (input ("Porcentaje Magro Del Paquete A: "))
ba = float (input ("Precio Por Libra Paquete B: "))
mb = float (input ("Porcentaje Magro Del Paquete B: "))
cla = pa/ma*100
clb = ba/mb*100
print("Costo Por Libra De Carne Del Paquete A: ",cla)
print("Costo Por Libra De Carne Del Paquete B: ",clb)
if cla > clb:
    print("El Paquete B Es El Mejor Valor")
else:
    print("El Paquete A Es El Mejor Valor")
