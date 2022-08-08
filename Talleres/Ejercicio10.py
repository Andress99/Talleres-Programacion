#Entradas
Chelines_Austriacos=int(input("Ingrese los Chelines"))
Dracmas_Griegos=int(input("Ingrese los Dracmas"))
Pesetas=int(input("Ingrese los Pesetas"))
#Caja Negra
Chelines_Pesetas=956871/100
Conversion_ChePe=(Chelines_Austriacos)*Chelines_Pesetas
Dracmas_Pesetas=88607/100
Conversion_DraPe=(Dracmas_Griegos)*Dracmas_Pesetas
Conversion_PeFrf=(Conversion_DraPe)/20110
Conversion_PeUSD=(Pesetas)/122499
LiraIta_Pesetas=9289/100
Conversion_PeLiIta=(Pesetas)*LiraIta_Pesetas
#Salida
print("Conversion de Chelines a Pesetas;   ",Conversion_ChePe)
print("Conversion de Dracmas a Franco;   ",Conversion_PeFrf)
print("Conversion de Pesetas a Dolar;   ",Conversion_PeUSD)
print("Conversion de Pesetas al Lira;   ",Conversion_PeLiIta)