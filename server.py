
from flask import Flask, render_template, request, redirect, session, flash, jsonify
import os, jinja2

app = Flask(__name__)

app.secret_key = '2345lkjhgf456'

@app.route('/')
def homepage():
    """shows the main page of the app"""

    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")