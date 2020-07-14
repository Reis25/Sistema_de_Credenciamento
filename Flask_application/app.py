from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Aplicação Flask executada com sucesso'


if __name__ == '__main__':
    app.run()
