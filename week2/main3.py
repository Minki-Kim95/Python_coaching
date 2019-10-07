"""
flask module
"""
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    """
    home of web
    :return: meter_yard.html
    """
    return render_template('meter_yard.html')

@app.route('/post', methods=['GET', 'POST'])
def post():
    """
    post value of input data which name is test
    :return: transfered yard data (if data is string, reload index again)
    """
    try:
        value = int(request.form['test'])
        yard_value = str(value * 1.09361)
        return yard_value + 'yard'

    except ValueError:
        return redirect(url_for('index')) # render_template('meter_yard.html')

    except:
        return 'undefined error is evoked'


if __name__ == '__main__':
    app.run()
