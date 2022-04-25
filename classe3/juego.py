from random import randint
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

		