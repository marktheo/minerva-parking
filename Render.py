from flask import Flask, request, render_template

#Flask Instance - Init
app = Flask(__name__)

#Main Page - About
@app.route("/")
def about():
    return render_template("About.html")

#Secondary Page - Register
@app.route("/register")
def register():
    return render_template("Register.html")

#Secondary Page - Login
@app.route("/login")
def login():
    return render_template("Login.html")

app.run()