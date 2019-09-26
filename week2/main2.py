"""
flask module
"""
from flask import Flask, render_template, request   # flask module

app = Flask(__name__)


@app.route('/')
def test():
    """
    home of web
    :return: hello.html
    """
    return render_template('hello.html')

@app.route('/post', methods=['POST'])
def post():
    """
    post value of input data which name is test
    :return: letter Hello world + input data
    """
    value = request.form['test']
    return 'Hello world ' + value

if __name__ == '__main__':
    app.run()
