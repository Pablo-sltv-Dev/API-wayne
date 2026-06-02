try:
    from flask import jsonify, request
    from functools import wraps
    from src import app, SECRET_KEY
    from .utils import extracion
    from .models import User
    import bcrypt
    import jwt
except Exception as erro:
    print("\nTipo de erro: ", Exception, "\nErro na :", erro )
def token_required(f):
    
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization") # vai ler o token
        if not token:
            return jsonify({"erro": "token ausente"}), 401
        try:
            token = token.split(" ")[1] # vai retirar o 'bearer'

            dados = jwt.decode(
                token,
                SECRET_KEY,
                algorithms=["HS256"]
            
            )
        except:
            return jsonify({"Erro":"Token inválido"}), 401
        
        return f(*args, **kwargs)
    return decorated 
    

@app.before_request
def verification():
    print(f"requisição para: {request.endpoint}")


@app.route('/rta/teste')
def connection_test():
    return jsonify({"menssage": "hello world"})

@app.route('/rta/log_test', methods=['POST'])
def verificacao_info():
    try:
        data = extracion(request.get_json())
        # saida :  {'email': 'teste@gmail.com', 'senha': 'senha1234'} 
        # print("\n",data,"\n")

        try:
            usuario = User(data)
            vrfccao = usuario.vrfcr()
            if vrfccao:
                return {"message":"rota com dados acessada", "token":vrfccao}
                    

        except Exception as erro:
            return {"Tipo": Exception, "erro": erro}

    

    except Exception as erro:
        print(f"Error:{erro}")
        return {"menssage": "algo deu errado", "Error": erro}
    

@app.route("/rta/teste_tk")
@token_required
def teste():
    return jsonify({"message":"Acesso com o token feito com sucesso"})









