import os
print('bienvenido a mi diario')
contraseña=input('porfavor ingrese la contraseña ')
if contraseña == 'hololo':
	on=True
	while on == True :
		opciones=input(""" que desea hacer ? :
			1.escribir
			2.borrar diario
			3.leer
			4.salir
			""")
		if opciones == "1":
			diario=open("diario.txt","a")
			escribir=input("ingrese el texto : ")
			diario.write(escribir)
			diario.close()
		elif opciones == "2":
			os.remove("diario.txt") 
		elif opciones == "3":
			diario=open("diario.txt","r")
			print(diario.read())
		elif opciones == "4":
			on=False
			print ('adios:)')
else :
	print ('la contraseña es incorecta')

