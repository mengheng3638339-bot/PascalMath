import os
from flask import Flask, render_template

template_dir = os.path.dirname(__file__)

app = Flask(__name__, template_folder=template_dir)


@app.route("/")
def index():
    return render_template("pascal.html")


# Vercel's Python runtime looks for a WSGI-compatible "app" object

if __name__ == "__main__":
    app.run(debug=True)
