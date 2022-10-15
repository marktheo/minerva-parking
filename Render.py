import sqlite3

sql = sqlite3.connect("database.db").cursor()

from flask import Flask, request, render_template 

app = Flask(__name__)

@app.route("/about")
def about():
    return render_template("About.html")

@app.route("/register")
def register():
    return render_template("Register.html")

@app.route("/login")
def login():
    return render_template("Login.html")

@app.route("/userlogin", methods = ["POST"])
def userlogin():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        return userlogin(username, password)
    else:
        return render_template("Login.html", errormessage = "Error 404")
        

@app.route("/dashboard")
def dashboard():
    return render_template("Dashboard.html")

@app.route("/schedule")
def schedule():
    return render_template("Schedule.html")

@app.route("/calendar")
def calendar():
    return render_template("Calendar.html")

app.run()