from main import app
from flask import render_template


@app.route('/')
def index():
    name = 'Ivan'
    return render_template('index.html', name=name)
