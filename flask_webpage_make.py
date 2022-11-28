from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello, World!</h1>"


@app.route("/second")
def second():
    return "This is <strong>Second</strong> Page!"


@app.route("/input/<args>")
def argin(args):
    return f"<h1>Hello, <strong style='color:red;'>{args}</strong>!</h1>"


if __name__ == "__main__":
    app.run("0.0.0.0", port=80)