from flask import jsonify, request
from src import app

@app.before_request
def verification():
    print(f"requisição para: {request.endpoint}")


@app.route('/rta/teste')
def connection_test():
    return jsonify({"menssage": "hello world"})

@app.route('rta/log/<email>/<senha>')
def verificacao_info(email, senha):
    return # aqui irá ficar as informações