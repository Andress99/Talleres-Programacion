#Entrada
#Matematicas
Examen_Math=float(input("Nota Examen Ma"))
Tarea_M1=float(input("Nota 1 Tarea Ma"))
Tarea_M2=float(input("Nota 2 Tarea Ma"))
Tarea_M3=float(input("Nota 3 Tarea Ma"))
#Fisica
Examen_Fisic=float(input("Nota Examen Fi"))
Tarea_F1=float(input("Nota 1 Tarea FI"))
Tarea_F2=float(input("Nota 2 Tarea Fi"))
#Quimica
Examen_Quimic=float(input("Nota Examen Qui"))
Tarea_Q1=float(input("Nota 1 Tarea Qui"))
Tarea_Q2=float(input("Nota 2 Tarea Qui"))
Tarea_Q3=float(input("Nota 3 Tarea Qui"))
#Caja Negra
ma=Examen_Math*0.90+((Tarea_M1+Tarea_M2+Tarea_M3)/3)*0.10
fi=Examen_Fisic*0.80+((Tarea_F1+Tarea_F2)/2)*0.20
qui=Examen_Quimic*0.85+((Tarea_Q1+Tarea_Q2+Tarea_Q3)/3)*0.15
Promedio=(ma+fi+qui)/3
#Salida
print (f"Matematicas{ma},Fisica{fi},Quimica{qui},el promedio de las materias es1 {Promedio}")