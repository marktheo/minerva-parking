import sqlite3
from Model import User
from CreateDB import connection, sql

#Verifies if the email exists. If not, the user is registered
def insertUser(name, phone, email, password):
    connection = sqlite3.connect('DataBase.db')
    sql = connection.cursor()
    rows = sql.execute('SELECT * FROM user;').fetchall()

    for row in rows:
        if(row[3] == email):
            return False

    sql.execute('INSERT INTO user (name, phone, email, password) VALUES (?, ?, ?, ?);', (name, phone, email, password))
    connection.commit()
    return True

def selectUser(email, password):
    connection = sqlite3.connect('DataBase.db')
    sql = connection.cursor()
    rows = sql.execute('SELECT * FROM user;').fetchall()

    for row in rows:
        if(row[3] == email and row[4] == password):
            user = User(row[0], row[1], row[2], row[3], row[4])
            return user

    return False