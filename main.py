#!/usr/bin/python3
from flask import Flask, render_template

app = Flask(__name__, template_folder='.')

@app.route('/')
def home():
    return render_template("home.html", pagetitle="Weather App")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9090, debug=True)
