from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def page():
    return render_template("Product.html")

app.run()