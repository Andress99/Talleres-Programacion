#Entrada
Horas_Trabajadas=int(input("Horas de trabajo"))
Valor_hora=int(input("Precio de la hora"))
#Caja Negra
Salario_Total=(Valor_hora)*Horas_Trabajadas
Descuento=Salario_Total*(20/100)
Salario_Neto=(Salario_Total-Descuento)
#Salida
print("El salario neto es;  ",Salario_Neto)