import sqlite3

connection = sqlite3.connect('database.db')
print('Opened database successfully');

connection.execute('CREATE TABLE movies (name TEXT, year TEXT, genre TEXT)')
print('Table created successfully');