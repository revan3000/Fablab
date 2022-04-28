from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3 as sql


app=Flask(__name__)

@app.route("/")
def home():
	Eliot="Eliot"
	return render_template("home.html",data=Eliot)

@app.route("/books")
def books():
 	con=sql.connect("db_web.db")
 	con.row_factory=sql.Row
 	cur=con.cursor()
 	cur.execute("select * from books")
 	data=cur.fetchall()

 	return render_template("books.html", data=data)

@app.route("/add_books",methods=['POST','GET'])
def add_books():
	if request.method == 'POST':
		name=request.form['name']
		author=request.form['author']
		year=request.form['year']
		con=sql.connect("db_web.db")
		cur=con.cursor()
		cur.execute("insert into books(name,author,year) values (?,?,?)",(name,author,year))
		con.commit()
		flash("book Added","success")
		return redirect(url_for("books"))

	return render_template("add_books.html")

@app.route("/edit_books/<string:id>", methods=["POST","GET"])
def edit_books(id):
	if request.method == 'POST':
		name=request.form['name']
		author=request.form['author']
		year=request.form['year']
		con=sql.connect("db_web.db")
		cur=con.cursor()
		cur.execute("update books set name=?, author=?, year=? where id=?",(name,author,year,id))
		con.commit()
		flash("book Update","success")
		return redirect(url_for("books"))
	con=sql.connect("db_web.db")
	con.row_factory=sql.Row
	cur=con.cursor()
	cur.execute("select * from books where id=?",(id,))
	data=cur.fetchone()

	return render_template("edit_books.html",data=data)

@app.route("/delet_book", methods=["GET"])
def delete_book(id):
	if request.method == "GET":
		on=sql.connect("db_web.db")
		con.row_factory=sql.Row
		cur=con.cursor()
		cur.execute("delete from book where ID=?",(id,))
		flash('Book Deleted','succes')

	return redirect(url_for("books"))







if __name__ == "__main__":
	app.secret_key='hololo'
	app.run(debug=True)

