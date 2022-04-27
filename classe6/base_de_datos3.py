import sqlite3
con = sqlite3.connect("test.db")
data = con.cursor()

data.execute("SELECT * FROM user;")

print(data.fetchall())
con.commit()
con.close()
