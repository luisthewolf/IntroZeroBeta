import math

v = float (input ("Introduzca La Velocidad Del Viento (mi/h): "))
t = float (input ("Introduzca La Temperatura En Grados Fahrenheit: "))
if (0 <= v <= 4):
    si = t
    print("Índice De Sensacion Termica: ",si)
elif (v >= 45):
    si = 1.6 * t - 55
    print("Indice De Sensacion Termica: ",si)
else:
    si = 91.4 + (91.4 - t)*(0.0203 * (math.sqrt (v) - 0.474))
    print("Indice De Sensacion Termica: ",si)
