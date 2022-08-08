#Entrada
Presupuesto=int(input("Presupuesto Anual"))
#Caja Negra
Descuento1=Presupuesto*(60/100)
Ginecologia=(Presupuesto-Descuento1)
Descuento2=Presupuesto*(70/100)
Traumatologia=(Presupuesto-Descuento2)
Pediatra=(Presupuesto-Descuento2)
Total=(Ginecologia+Traumatologia+Pediatra)
#Salida
print("Presupuesto Ginecologia:   ",Ginecologia)
print("Presupuesto Traumatologia:   ",Traumatologia)
print("Presupuesto Pediatria:   ",Pediatra)
print("Presupuesto Total:   ",Total)