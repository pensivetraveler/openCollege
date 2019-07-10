from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/hello/<name>')
def index(name):
    return "Hello " + name


@app.route('/profile')
def profile():
    age = request.args.get('age')
    return "My age is " + age


if __name__ == '__main__':
    app.run()
