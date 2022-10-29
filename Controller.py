import sqlite3
import qrcode
from model.Client import client
from model.Vehicle import vehicle

#Verifies if the email exists.
def findClient(email):
    try:
        connection = sqlite3.connect('database.db')
        sql = connection.cursor()
        sql.execute('CREATE TABLE IF NOT EXISTS client([id] INTEGER PRIMARY KEY AUTOINCREMENT, [name] TEXT, [phone] TEXT, [email] TEXT UNIQUE, [password] TEXT, [registered_in] TEXT DEFAULT CURRENT_TIMESTAMP);')
        rows = sql.execute('SELECT * FROM client;').fetchall()

        for row in rows:
            if(row[3] == email):
                return True
        
        return False
    
    except Exception as e:
        print(e)

    finally:
        connection.commit()
        connection.close()

#Verifies if the vehicle exists.
def findVehicle(plate):
    try:
        connection = sqlite3.connect('database.db')
        sql = connection.cursor()
        sql.execute('CREATE TABLE IF NOT EXISTS vehicle([id] INTEGER PRIMARY KEY AUTOINCREMENT, [brand] TEXT, [model] TEXT, [color] TEXT, [plate] TEXT UNIQUE, [registered_in] TEXT DEFAULT CURRENT_TIMESTAMP);')
        rows = sql.execute('SELECT * FROM vehicle;').fetchall()

        for row in rows:
            if(row[4] == plate):
                return True
        return False
    
    except Exception as e:
        print(e)

    finally:
        connection.commit()
        connection.close()

#Inserts the client into database
def createClient(name, phone, email, password):
    try:
        connection = sqlite3.connect('DataBase.db')
        sql = connection.cursor()
        sql.execute('INSERT INTO client (name, phone, email, password) VALUES (?, ?, ?, ?);', (name, phone, email, password))

    except Exception as e:
        print(e)

    finally:
        connection.commit()
        connection.close()

#Inserts the vehicle into database
def createVehicle(brand, model, color, plate):
    try:
        connection = sqlite3.connect('DataBase.db')
        sql = connection.cursor()
        sql.execute('INSERT INTO vehicle (brand, model, color, plate) VALUES (?, ?, ?, ?);', (brand, model, color, plate))

    except Exception as e:
        print(e)

    finally:
        connection.commit()
        connection.close()

#Verifies if the login provided informations are correct
def readClient(email, password):
    try:
        connection = sqlite3.connect('DataBase.db')
        sql = connection.cursor()
        rows = sql.execute('SELECT * FROM client;').fetchall()

        for row in rows:
            if(row[3] == email and row[4] == password):
                logClient(row[0])
                return True
        return False
    
    except Exception as e:
        print(e)

    finally:
        connection.commit()
        connection.close()


def logClient(id):
    try:
        connection = sqlite3.connect('DataBase.db')
        sql = connection.cursor()
        rows = sql.execute('SELECT * FROM client WHERE id=?', (str(id))).fetchall()

        for row in rows:
            client.setId(row[0])
            client.setName(row[1])
            client.setPhone(row[2])
            client.setEmail(row[3])
            client.setPassword(row[4])
            client.setState(True)

        rows = sql.execute('SELECT * FROM vehicle WHERE id=?', (str(id))).fetchall()

        for row in rows:
            vehicle.setBrand(row[1])
            vehicle.setModel(row[2])
            vehicle.setColor(row[3])
            vehicle.setPlate(row[4])
    
    except Exception as e:
        print(e)

    finally:
        connection.commit()
        connection.close()

def clientQrcode(client):
    card = 'BEGIN:VCARD\r\nVERSION:3.0\r\nFN:'+client.getName()+'\r\nTEL;TYPE=Telefone:'+client.getPhone()+'\r\nEMAIL;TYPE=E-mail:'+client.getEmail()+'\r\nEND:VCARD\r\n'
    image = qrcode.make(card)
    image.save("./static/media/Qrcode"+str(client.getId())+".jpeg")