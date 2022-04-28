import sqlite3 as sql

con=sql.connect('db_web.db')
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS books")
sql="""CREATE TABLE "books"(
"id" INTEGER PRIMARY KEY AUTOINCREMENT,
"name" TEXT,
"author" TEXT,
"year" TEXT
)"""

cur.execute(sql)
con.commit()
con.close()

