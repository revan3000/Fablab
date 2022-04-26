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