from random import randint
contraseña='hololo'
def mi_bar():
	edad=input ('que edad tienes ?')
	edad=int(edad)
	if edad < 18 or edad > 60:
		print ('usted no tiene la edad requerida para entrar')
	if edad >= 18:
		print ('menu')
		x=['vino','cerveza']
		for b in x :
			print (b)
		usuario=input ('que desea tomar ?')
		if usuario==x[0]:
			print ('*entregar copa de vino*')
		elif usuario==x[1]:
			print ('*entregar vaso de cerveza*')
		else:
			print ('esta opcion no esta disponoble en este bar')
def mi_juego():
	x=['piedra','papel','tijera']
	partida=True 
	while partida == True:
		computer = x[randint(0,2)]
		usuario=input('piedra, papel, o tijera ?')
		print (usuario, computer)
		if usuario == computer:
			print ('Empate !')
		elif usuario == 'piedra':
			if computer == 'papel':
				print('Perdiste !')
			else:
				print ('ganaste')
		elif usuario == 'papel':
			if computer == 'tijera':
				print ('perdiste')
			else:
				print ('ganaste')
		elif usuario == 'tijera':
			if computer == 'piedra':
				print ('Perdiste!')
			else:
				print ('ganaste')
		elif usuario == 'salir':
			partida=False
		else:
			print ('error opcion no valida')
def pokedex():
	print ('bienvenido al pokedex de Eliot')
	pokemon1='pikachu'
	pokemon2='decidueye'
	pokemon3='pachirisu'
	pokedex=[pokemon1,pokemon2,pokemon3]
	on1=True
	while on1 == True:

		print ('pokemones en el pokedex:')
		for pokemon in pokedex:
			print (pokemon)
		pokemonNuevo=input ('agregar nuevo pokemon o salir:')
		if pokemonNuevo == 'salir':
			on1=False
		else:
			pokemon4=pokemonNuevo
			print (pokemon4)
			pokedex.append(pokemon4)
			print ('pokemones en el pokedex:')
			for pokemon in pokedex:
				print (pokemon)
		


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
			mi_bar()
		elif usuario == '2':
			mi_juego()
		elif usuario == '3':
			pokedex()
		elif usuario == '4':
			print ('salir')
			on=False

	else:
		print ('error')
		on=False
