import os
from flask import Flask, render_template

template_dir = os.path.join(os.path.dirname(__file__), "..", "templates")

app = Flask(__name__, template_folder=template_dir)


@app.route("/")
def index():
    return render_template("pascal.html")


# Vercel's Python runtime looks for a WSGI-compatible "app" object
