import requests 

resultado=requests.get("https://swapi.dev/api/people")
busqueda=input("ingrese el nombre del personage que busca")
data=resultado.json()
personages=data["results"]
for p in personages:
	if p["name"] == busqueda:
		print ("personage encontrado"+p["name"])
		print ("El personage sale en estas peliculas:")
		for pelicula in p["films"]:
			print (pelicula)

	else:
		print ("personage no encontrado")