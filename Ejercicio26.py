#Ejercicio 26, Imprime la suma del número actual y el número anterior

numero_actual=int(input("Ingrese un número: "))

#se suma el número ingresado más el mismo número restado 1
suma=numero_actual+(numero_actual-1)
print("La suma del actual ingresado más el anterior es: "+str(suma))