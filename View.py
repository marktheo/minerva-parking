from flask import Flask, request, render_template
from Controller import insertUser, selectUser, User

#Flask Instance - Init
app = Flask(__name__)

#About Page
@app.route("/")
def about():
    return render_template("About.html")

#Register Page
@app.route("/register")
def register():
    return render_template("Register.html")

#Register Controller
@app.route("/registerUser", methods = ["POST"])
def registerUser():
    name = request.form["name"]
    phone = request.form["phone"]
    email = request.form["email"]
    password = request.form["password"]

    if(insertUser(name, phone, email, password) == True):
        return login()
    else:
        return register()

#LoginPage
@app.route("/login")
def login():
    return render_template("Login.html")

#Login Controller
@app.route("/loginUser", methods = ["POST"])
def loginUser():
    email = request.form["email"]
    password = request.form["password"]

    if(selectUser(email, password) == True):
        return about()
    else:
        return login()

#Runs the Application
app.run()