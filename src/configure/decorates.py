from src import app
from flask import jsonify, request, make_response
from ..utils import extracion, Alert_Info,Alert_Debug,Alert_Warning,Alert_Error,Alert_Success, Alert_Critical
# from ..configure import *

try:

    @app.before_request # Puxa antes de acessar cada requisição
    def verification():
        try: 
            print(f'''\n
Esse é o Method  { request.method }

Esse é o Host -> { request.host }

Esse é o content-Type -> { request.content_type }

Esse é o User-Agent -> { request.user_agent }
Esse é o Accept -> 
Esse é o Path -> { request.path }

Essa é a URL -> {request.url}

Essa é a scheme -> {request.scheme}

Esse é o IP do Cliente{request.remote_addr}

Esse é o ARGS {request.args}


\n''')
            if not request.endpoint:
                Alert_Error("Rota Inexistente")
                raise page_not_ide(404)

        except Exception as erro:
            return jsonify({"Menssage": Exception, "message": erro})
        

    @app.after_request
    def response(response):
        print(f'''
.
              response -> { response }
              Status -> {response.status_code}
''')
        # saida:  Esse é o Host -> { request.host }
        return response
    





    @app.errorhandler(404)
    def page_not_ide(error):
        Alert_Error("Erro 404")
        return jsonify({"Error":"Pagina não encontrada", "number":error})
    @app.errorhandler(500)
    def error_intern(error):
        return jsonify({"Error":"Erro interno", "number":error})
        
except Exception as error:
    print(f"\nTipo de erro: {Exception}\nErro na:{error}\n")
    Alert_Critical("Erro interno")