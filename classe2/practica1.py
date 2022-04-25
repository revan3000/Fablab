#aqui voy a hacer mi primera practica
print ('bienvenido al pokedex de Eliot')
pokemon1='pikachu'
pokemon2='decidueye'
pokemon3='pachirisu'
pokedex=[pokemon1,pokemon2,pokemon3]
print ('pokemones en el pokedex:')
for pokemon in pokedex:
	print (pokemon)
pokemon4=input ('agregar nuevo pokemon:')
pokedex.append(pokemon4)
print ('pokemones en el pokedex:')
for pokemon in pokedex:
	print (pokemon)
