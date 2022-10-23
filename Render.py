from flask import Flask, request, render_template

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

#LoginPage
@app.route("/login")
def login():
    return render_template("Login.html")

#Runs the Application
app.run()