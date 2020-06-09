
print ("""************
Calculadora
************
Menu
1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Salir""")

opcion=int(input("Elige la opción: "))

if opcion==5:
	print("Gracias por usar mi calculadora")

else:

	x=int(input("Ingrese el primer número: "))
	y=int(input("Ingrese el segundo numero: "))

if opcion==1:
	print("La suma es: ",x+y)

elif opcion==2:
	print("La resta es: ",x-y)

elif opcion==3:
	print("La Multiplicacion es: ",x*y)

elif opcion==4:
	print("La Division es: ",x/y)