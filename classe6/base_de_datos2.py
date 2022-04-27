import sqlite3
con = sqlite3.connect("test.db")
data = con.cursor()

data.execute("INSERT INTO user('name','lastname','age') VALUES ('Eliot','Boniface',16);")
con.commit()
con.close()


