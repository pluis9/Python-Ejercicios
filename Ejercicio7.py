#Ejercicio 7, Ingresar un valor en dólares y transformar en Euros y Yen.
valor_dolar=float(input("Ingrese un valor en dólares: "))

#se convierte a euro
valor_euro=valor_dolar*0.96
#se convierte a yen
valor_yen=valor_dolar*128.89
print("La conversión a euros es: "+str(valor_euro))
print("La conversión a yenes es: "+str(valor_yen))