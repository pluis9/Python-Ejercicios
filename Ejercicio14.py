#Ejercicio 14, Ingresar la longitud en centímetros y convertirla en metro y kilómetro.

centimetro=int(input("Ingrese la longitud en centímetros: "))
#se convierte a metros
metro=(centimetro*0.01)

#se convierte a kilómetrometros
kilometro= (centimetro*0.00001)

print("La longitud en metros es : "+str(metro))
print("La longitud en kilómetros es : "+str(kilometro))