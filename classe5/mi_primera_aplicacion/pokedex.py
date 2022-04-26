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