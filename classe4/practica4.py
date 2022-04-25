import csv
import os
print('bienvenido a la lista de campeones')
contraseña=input('porfavor ingrese la contraseña ')
if contraseña == 'hololo':
	on=True
	while on == True :
		opciones=input(""" que desea hacer ? :
			1.ver campeones
			2.añadir campeones
			3.borrar campeones
			4.salir
			""")
		if opciones == "1":
			with open("campeones.csv") as campeones:
				read= csv.DictReader(campeones)
				for c in read:
					print(c.values())
		elif opciones == "2":
			with open("campeones.csv","w") as campeones:

				x =csv.writer(campeones)
				x.writerow(["name","classe","linea","daño"])
				new_champ=[]
				name=input("escribe el nombre del campeon")
				new_champ.append(name)
				classe=input("escribe la clase del campeon")
				new_champ.append(classe)
				linea=input("escribe la linea del campeon")
				new_champ.append(linea)
				daño=input("escribe el typo de daño que haga el campeon")
				new_champ.append(daño)
				x.writerow(new_champ)
		elif opciones == "3":
			diario=open("diario.txt","r")
			print(diario.read())
		elif opciones == "4":
			on=False
			print ('adios:)')
else :
	print ('la contraseña es incorecta')

