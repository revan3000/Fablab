import sqlite3
con = sqlite3.connect("test.db")
data = con.cursor()
class Juegos:
	def __init__(self,name,description,precio,tamaño,desarolladora):
		self.name=name
		self.description=description
		self.precio=precio
		self.tamaño=tamaño
		self.desarolladora=desarolladora

def ver_ojetos():
	data.execute("SELECT * FROM user;")
	print (data.fetchall())

def agregar_objetos():
	data.execute("""INSERT INTO juegos('name','description','precios','tamaño','Desarolladora') VALUES ('Screep',"Es un MMO RTS","15$","10G",");")
	data.execute("""INSERT INTO juegos('name','description','precios','tamaño','Desarolladora') VALUES 
	(:name,:description,:age)""",{'name':user_1.name,'lastname':user_1.lastname,'age':user_1.age} )

con.commit()
con.close()