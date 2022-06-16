import json
from flask import Flask, render_template
app = Flask(__name__)

f = open('./representation.json')
data = json.load(f)

@app.route("/")
def display():
    return render_template('index.html', data=data)
