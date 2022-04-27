import folder
import sqlite3
con = sqlite3.connect("test.db")
data = con.cursor()


user_1=folder.User('Eliot','Boniface',16)
print(user_1.name)
data.execute("""INSERT INTO user('name','lastname','age') VALUES (:name,:lastname,:age)""",{'name':user_1.name,'lastname':user_1.lastname,'age':user_1.age} )
con.commit()
data.execute("SELECT * FROM user;")
print(data.fetchall())

con.close()