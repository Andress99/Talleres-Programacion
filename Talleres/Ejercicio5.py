#Entrada
Parcial_1=float(input("Nota parcial 1:"))
Parcial_2=float(input("Nota parcial 2:"))
Parcial_3=float(input("Nota parcial 3:"))
Examen_Final=float(input("Nota de examen:"))
Trabajo_Final=float(input("Nota trabajo final:"))
#Caja Negra
Promedio_1=(Parcial_1+Parcial_2+Parcial_3)/3*0.55
Promedio_2=(Examen_Final)*0.30
Promedio_3=(Trabajo_Final)*0.15
Nota_Final=(Promedio_1+Promedio_2+Promedio_3)
#Salida
print("Nota Final;  ",Nota_Final)