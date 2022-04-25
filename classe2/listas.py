#aqui estoy aprendiendo a usar listas 
campeones=['vladimir','akali','jayce'] 
print (campeones)
print (campeones[0])
campeones[2]='katarina'
print (campeones)
campeones.append('jhin')
print (campeones)
campeones2=['akshan','talon']
campeones.extend(campeones2)
print (campeones)
campeones.pop(3)
print (campeones)
tuplacampeones= ('vladimir','jayce')
x=list(tuplacampeones)
x[1]='akali'
#aqui estoy aprendiendo a usar tuplas
tuplacampeones=tuple(x)
print (tuplacampeones)
jayce,akali=tuplacampeones
print (jayce,akali)
#aqui estoy aprendiendo a usar sets
setcampeones={'jayce','akali'}
for campeones in setcampeones :
	print (campeones)
	print ('hola que tal')
setcampeones.add('vladimir')
print (setcampeones)
y=('fizz','urgot')
setcampeones.update(y)
print (setcampeones)
setcampeones.remove('urgot')
print (setcampeones)
#aqui estoy aprendiendo a usar dictionarios
campeon={
	'nombre':'vladimir',
	'descripcion': """e gusta jugar vladimir porque es un mago assesino""",
	'classe':'midlaner'}
campeon1=campeon['nombre']
print (campeon1)
print (campeon.get('classe'))
print (campeon.values())
print (campeon.keys())
print (campeon.items())
campeon.update({'classe':'toplaner'})
print (campeon.values())
campeon.pop('descripcion')
print (campeon.keys())
