from flask import Flask, render_template, request

app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello World!'

@app.route('/')
def test():
    return render_template('hello.html')

@app.route('/post', methods=['POST'])
def post():
    value = request.form['test']
    return 'Hello world ' + value

if __name__ == '__main__':
    app.run()