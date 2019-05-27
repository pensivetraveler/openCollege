from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/healthCheck')
def health_check():
    return 'ok'


if __name__ == '__main__':
    app.run()
