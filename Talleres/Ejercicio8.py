import math
#Entradas
Lado_a=float(input("Digite lado a:"))
Lado_b=float(input("Digite lado b:"))
Lado_c=float(input("Digite lado c:"))
#Caja Negra
s=(Lado_a+Lado_b+Lado_c)/2
Area=math.sqrt(s*(s-Lado_a)*(s-Lado_b)*(s-Lado_c))
#Salida
print (("Area;  ",Area))