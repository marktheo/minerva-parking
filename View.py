from flask import Flask, request, render_template
from Controller import findClient, findVehicle, createClient, createVehicle, readClient, clientQrcode
from model.Client import client
from model.Vehicle import vehicle

#Flask Instance - Init
app = Flask(__name__)

#About Page
@app.route("/")
def about():
    return render_template("About.html")

#Register Page
@app.route("/register")
def register():
    return render_template("RegisterUser.html")

#Register User Controller
@app.route("/register_", methods = ["POST"])
def registerUser():
    name = request.form["name"]
    phone = request.form["phone"]
    email = request.form["email"]
    password = request.form["password"]

    if(findClient(email) == False):
        client.setName(name)
        client.setPhone(phone)
        client.setEmail(email)
        client.setPassword(password)

        return render_template("RegisterVehicle.html")
    else:
        return register()

#Register Vehicle Controller
@app.route("/register__", methods = ["POST"])
def registerVehicle():
    brand = request.form["brand"]
    model = request.form["model"]
    color = request.form["color"]
    plate = request.form["plate"]

    if(findVehicle(plate) == False):
        createClient(client.getName(), client.getPhone(), client.getEmail(), client.getPassword())

        vehicle.setBrand(brand)
        vehicle.setModel(model)
        vehicle.setColor(color)
        vehicle.setPlate(plate)

        createVehicle(vehicle.getBrand(), vehicle.getModel(), vehicle.getColor(), vehicle.getPlate())
        return login()

    else:
        return register()

#Login Page
@app.route("/login")
def login():
    return render_template("Login.html")

#Login Controller
@app.route("/login_", methods = ["POST"])
def loginUser():
    email = request.form["email"]
    password = request.form["password"]

    if(readClient(email, password) == True):
        clientQrcode(client)
        return dashboard(client.getState())
    else:
        return render_template("Login.html")

#Dashboard Page
@app.route("/dashboard")
def dashboard(log):
    if(log == True):
        return render_template("Dashboard.html", client = client, vehicle = vehicle)
    else:
        return login()

app.run()