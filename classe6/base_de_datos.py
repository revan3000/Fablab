import sqlite3
con = sqlite3.connect("test.db")
data = con.cursor()
data.execute("""CREATE TABLE 'user'(
	'id' INTEGER PRIMARY KEY AUTOINCREMENT,
	'name' VARCHAR,
		'lastname' VARCHAR,
		'age' INTEGER);
	""")
con.commit()
con.close()






