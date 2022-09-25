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