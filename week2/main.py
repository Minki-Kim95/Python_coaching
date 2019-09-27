"""
flask module
"""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    """
    home
    :return: just Hello world
    """
    return "Hello World!"


if __name__ == "__main__":
    app.run(host='localhost', port=3000)
