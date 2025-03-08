from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def bye():
    return "<p>Bye, World!</p>"

@app.route("/username/<name>/<int:number>")
def great(name, number):
    return f"Hello, {name}, you are {number} years old."


if __name__ == "__main__":
    app.run(debug=True)
