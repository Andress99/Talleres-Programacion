#Entrada
Lectura_actual=float(input("Ultima Lectura"))
Lectura_anterior=float(input("Penultima Lectura"))
#Caja Negra
Variacion_lectura=Lectura_actual-Lectura_anterior
Costo_Total=(Variacion_lectura)*611
#Salida
print("Valor Factura; $ ",Costo_Total)