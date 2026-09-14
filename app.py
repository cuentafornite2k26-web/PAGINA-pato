from flask import Flask, render_template, send_from_directory
from pathlib import Path

app = Flask(__name__)
IMAGE_FOLDER = Path(__file__).parent / "imagenes"


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/imagenes/<path:filename>")
def imagenes(filename):
    return send_from_directory(IMAGE_FOLDER, filename)


if __name__ == "__main__":
    app.run(debug=True)
