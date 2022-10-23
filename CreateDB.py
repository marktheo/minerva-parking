import sqlite3

connection = sqlite3.connect('DataBase.db')

sql = connection.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS user([id] INTEGER PRIMARY KEY AUTOINCREMENT, [name] TEXT, [phone] TEXT, [email] TEXT UNIQUE, [password] TEXT);')

connection.commit()