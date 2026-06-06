try:
    from src import app, SECRET_KEY, logger, limiter
    from flask import jsonify, request
    from functools import wraps
    from .utils import extracion, Alert_Info,Alert_Debug,Alert_Warning,Alert_Error,Alert_Success, Alert_Critical
    from .models import User

    import jwt
    

    from .test import *




    
    # @app.route('/rta/teste')
    # @limiter.limit('5 per minute')
    # def connection_test():
    #     return jsonify({"menssage": "hello world"})



    @app.route('/rta/teste_info', methods=['POST'])    
    def request_info():
        
        data = extracion(request.get_json())
        if not data:
            return jsonify({"message": "dados inexistentes"})
        else:
            pass


        return jsonify({"message":data})


    @app.route('/rta/login', methods=['POST'])
    def verificacao_info():
        try:
            data = extracion(request.get_json())
            
            usuario = User(data)
            vrfccao = usuario.vrfcr()
            if vrfccao:
                return jsonify({"message":"rota com dados certos acessada", "token":vrfccao}) 
            else:
                return  jsonify({"message": "informações incorretas"})       
        except TypeError as erro:
            return jsonify({"menssage": "algo deu errado", "Error": erro})
        except Exception as erro:
            print(f"Error:{erro}")
            return {"menssage": "algo deu errado", "Error": erro}
        
    # ____________________________________
  






except Exception as erro:
    print(f"\n{Alert_Critical("Erro interno")}\nTipo de erro: {Exception}\nErro na:{erro}\n")


except Exception as erro:
    print(f"\n{Alert_Critical("Erro interno")}\nTipo de erro: {Exception}\nErro na:{erro}\n")

try:

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
except Exception as erro:
    print(f"\n{Alert_Critical("Erro interno")}\nTipo de erro: {Exception}\nErro na:{erro}\n")

    


try:
    @app.route('/rta/teste_tk', methods=['GET']) # essa rota só poder ser acessa se tiver o token
    @token_required
    def home():
        return jsonify({"message":"Acesso com o token feito com sucesso"})
 
except Exception as erro:
    print(f"\n{Alert_Critical("Erro interno")}\nTipo de erro: {Exception}\nErro na:{erro}\n")




