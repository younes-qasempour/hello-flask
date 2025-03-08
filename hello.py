from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def bye():
    return "<p>Bye, World!</p>"

@app.route("/username/<name>")
def great(name):
    return f"Hello, {name}"


if __name__ == "__main__":
    app.run(debug=True)
