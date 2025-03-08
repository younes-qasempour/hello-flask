from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return ("<h1 style='text-align: center'>Hello, World!</h1>"
            "<p>Thus is a paragraph</p>"
            "<img src='https://media.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif?cid=790b7611owv4b1jws6a9yrrf97r02tyt"
            "7biyio3nh05cmucz&ep=v1_gifs_search&rid=giphy.gif&ct=g' width=200>")

@app.route("/bye")
def bye():
    return "<p>Bye, World!</p>"

@app.route("/username/<name>/<int:number>")
def great(name, number):
    return f"Hello, {name}, you are {number} years old."


if __name__ == "__main__":
    app.run(debug=True)
