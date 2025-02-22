from flask import Flask, request, render_template, redirect, session, url_for, jsonify
import sqlite3 as sql

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret key'

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
   app.run(debug=True) 