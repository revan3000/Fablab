from random import randint
import piedra_papel_tijera
import bar
import pokedex

contraseña='hololo'
user_password=input('ingresar contraseña : ')
on=True
while on == True:
	if contraseña == user_password:
		print ("""bienvenido al bar 
			estas son nustras opciones : 
			1. bar 
			2. piedra papel o tijera
			3. pokedex
			4. salir  
			""")
		usuario=input('que deseas hacer ? ')
		if usuario == '1':
			bar.mi_bar()
		elif usuario == '2':
			piedra_papel_tijera.mi_juego()
		elif usuario == '3':
			pokedex.pokedex()
		elif usuario == '4':
			print ('salir')
			on=False

	else:
		print ('error')
		on=False