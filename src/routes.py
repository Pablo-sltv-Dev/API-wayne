try:
    from flask import jsonify, request, redirect, url_for
    from src import app, SECRET_KEY, logger
    from functools import wraps
    from .utils import extracion
    from .models import User

    import jwt
    from loguru import logger


except Exception as erro:
    print("\nTipo de erro: ", Exception, "\nErro na :", erro )

@app.before_request # Puxa antes de acessar cada requisição
def verification():
    try:
        # token = request.headers.get('Authorization')

        if not request.endpoint:
            logger.warning("Rota desconhecida")
            return jsonify({"Message":"Essa rota nao existe","Error": 404}, 404)
        
        if request.method == 'GET' and request.endpoint:
            logger.info("utilizando o GET")
            logger.warning('ATENÇÃO! URL acessou rota sem token!')
        if request.method == 'GET' and request.endpoint:
            logger.info("rota acessada utilizando Token com metodo GET")
            
        if request.method == 'POST' and request.endpoint:
            logger.info(f"utilizando o POST e o endpoint acessado foi {request.endpoint}")
        

    except Exception as erro:
        return jsonify({"Menssage": Exception, "message": erro})





def tipos_de_saida():
    logger.debug('Debug: Rota / acessada')
    logger.info('info: Processando Requisição')
    logger.warning('Warning: Atenção')
    return

#__________ token __________________    
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        
        token = request.headers.get("Authorization") # vai ler o token
        print(f"\ntoken sem filtro: {token}\n")
        if not token:
            return jsonify({"erro": "token ausente"}), 401
        try:
            token = token.replace("Bearer ", "") # vai retirar o 'bearer'
            print(token)
            # print("\n-\n",token)
            # dados = jwt.decode()
            # ide = dados['id']
            # print("\n",dados,"\n->")
            dados = jwt.decode(token,SECRET_KEY,algorithms=["HS256"])
            print(dados)
            # return jsonify({"message":"hum"})
            return f(*args, **kwargs)
        
        except jwt.ExpiredSignatureError:
            print("❌ Token expirado")
            return None
        except jwt.InvalidSignatureError:
            print("❌ Assinatura inválida ")
            return None
        except jwt.DecodeError:
            print("❌ Erro ao decodificar")
            return None
        except jwt.InvalidTokenError as e:
            print(f"❌ Erro: {e}")
            return None
    return decorated 
#____________________________________    



   
@app.route('/rta/teste')
def connection_test():
    return jsonify({"menssage": "hello world"})





@app.route('/rta/login', methods=['POST'])
def verificacao_info():
    try:
        data = extracion(request.get_json())
        print(f"\ninfo: {data}")
        # saida : { "message": "rota com dados acessada",
   # "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZW1haWwiOiJ0ZXN0ZUBnbWFpbC5jb20iLCJleHAiOjE3ODA2NTkxODl9.0_AMCvAIcT46P94d-M8WuQ32YA-X7bD9gjcT4fIJd0w"


        try:
            usuario = User(data)
            vrfccao = usuario.vrfcr()
            if vrfccao:
                return jsonify({"message":"rota com dados certos acessada", "token":vrfccao}) 
            else:
                return  jsonify({"message": "informações incorretas"})       

        except Exception as erro:
            return {"Tipo": Exception, "erro": erro}

    

    except Exception as erro:
        print(f"Error:{erro}")
        return {"menssage": "algo deu errado", "Error": erro}
    
# ____________________________________
@app.route('/rta/teste_tk', methods=['GET']) # essa rota só poder ser acessa se tiver o token
@token_required
def home():
    return jsonify({"message":"Acesso com o token feito com sucesso"})









