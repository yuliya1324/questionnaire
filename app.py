from flask import Flask
import datetime
from flask import url_for, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def instruction():
    return render_template('main.html')


@app.route('/statistics')
def stat():
    return render_template('statistics.html')


@app.route("/questionnaire")
def quest():
    return render_template('quest.html')


if __name__ == '__main__':
    app.run(debug=False)
