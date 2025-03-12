from flask import Flask, request, render_template, redirect, session, url_for, jsonify
import sqlite3 as sql

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret key'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True) 