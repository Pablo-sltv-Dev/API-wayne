try:
    from src import app, SECRET_KEY, logger, limiter
    from flask import jsonify, request
    from functools import wraps
    from .utils import extracion, Alert_Info,Alert_Debug,Alert_Warning,Alert_Error,Alert_Success, Alert_Critical
    from .models import User

    import jwt
    from .configure import token_required

    from .test import *




    
    



    @app.route('/rta/teste_info', methods=['POST'])    
    def request_info():
        
        data = extracion(request.get_json()) # extrai as informações
        print(f'''
            Email -> {data['email']}
            senha -> {data['senha']}
    ''')
        if not data:
            return jsonify({"message": "dados inexistentes"})
        else:
            return jsonify({"message":data}),200


        


    @app.route('/rta/login', methods=['POST'])
    def verificacao_info():
        try:
            data = extracion(request.get_json()) # Extrai as informações
            
            usuario = User(data)
            vrfccao = usuario.vrfcr() # aqui vai verificar as informações
            if vrfccao:
                return jsonify({"message":"rota com dados certos acessada", "dds": vrfccao}), 201 
            # Vai aparecer pro front
            # {
            #     "name": "nome",
            #     "email": "email",
            #     "token":"token"
            # }
            else:
                return  jsonify({"message": False}), 400       
        except TypeError as erro:
            return jsonify({"menssage": "algo deu errado", "Error": erro})
        except Exception as erro:
            print(f"Error:{erro}")
            return {"menssage": "algo deu errado"}
        



except Exception as erro:
    print(f"\n{Alert_Critical("Erro interno")}\nTipo de erro: {Exception}\nErro na:{erro}\nLinha: 62")



try:
    @app.route('/rta/teste_tk', methods=['GET']) # essa rota só poder ser acessa se tiver o token
    @token_required
    def home():
        return jsonify({"message":"Acesso com o token feito com sucesso"}),200
 
except Exception as erro:
    print(f"\n{Alert_Critical("Erro interno")}\nTipo de erro: {Exception}\nErro na:{erro}\nLinha: 89")




