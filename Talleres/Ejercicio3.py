#Entrada
Sueldo_Base=int(input("Digite su sueldo base:"))
#Caja Negra
comisiones= Sueldo_Base*(10/100)
aumento= comisiones*3
total= Sueldo_Base+aumento
#Salidas
print("Aunmento; ",aumento)
print("Total;  ",total)