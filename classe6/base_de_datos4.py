	import sqlite3
	con = sqlite3.connect("test.db")
	data = con.cursor()

	data.execute("""UPDATE user SET age=17 WHERE name="Eliot";""")
	data.execute("SELECT * FROM user;")
	print(data.fetchall())
	con.commit()
	con.close()
