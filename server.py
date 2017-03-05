from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

connection = sqlite3.connect('database.db')
print('Opened database Successfully')

connection.execute('CREATE TABLE IF NOT EXISTS posts (title TEXT, post TEXT)')

print('Table created Successfully')
connection.close()

@app.route('/')
def route():
	return render_template('home.html')

@app.route('/addnew')
def addnew():
	return render_template('newmovie.html')


@app.route('/addmovie', methods=['POST'])
def addmovie():
	connection = sqlite3.connect('database.db')
	cursor = connection.cursor()
	print('hi')
	try:
		name = request.form['name']
		year = request.form['year']
		genre = request.form['genre']
		cursor.execute('INSERT INTO movies (name, year, genre) VALUES (?,?,?)', (name, year, genre))
		connection.commit()
		message = 'Record succesfully added'
	except:
		connection.rollback()
		message = 'error in insert operation'
	finally: 
		return render_template('result.html', message = message)
		connection.close()
		

		


@app.route('/movies')
def movies():
	connection = sqlite3.connect('database.db')
	cursor = connection.cursor()
	cursor.execute('SELECT * FROM movies')
	movie_list = cursor.fetchall()
	connection.close()
	return jsonify(movie_list)

app.run(debug = True)
