class MyClass:
	nombre="Eliot"

data=MyClass()
print(data)

class Person:
	city = "Francia"
	def __init__(self,name,age):
		self.name=name
		self.age=age

	def myname(self):
		print("hello my name is " + self.name)


class Student(Person):
	def __init__(self,name,age,year):
		super().__init__(name,age)
		self.graduationyear=year
p1=Student("Eliot",16,2022)
print(p1.graduationyear)																																			
p1.myname()

class Campeon():
	gold=0
	def __init__(self,name,lane,damage):
		self.name=name
		self.lane=lane
		self.damage=damage
	
	def minionkill(self):
		self.gold=self.gold+13
		print(self.gold)


champ=Campeon("Vladimir","mid","ap")																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																							
champ.minionkill()
champ.minionkill()																												
champ.minionkill()
champ.minionkill()
champ.minionkill()
champ.minionkill()
champ.minionkill()
champ.minionkill()
champ.minionkill()
																																				
