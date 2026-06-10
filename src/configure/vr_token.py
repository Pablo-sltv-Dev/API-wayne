try:
    from src import app, SECRET_KEY, logger, limiter
    from flask import jsonify, request
    from functools import wraps
    import jwt

    from ..utils import extracion, Alert_Info,Alert_Debug,Alert_Warning,Alert_Error,Alert_Success, Alert_Critical
    # from .models import User
    def token_required(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = request.headers.get("Authorization") # vai ler o token
            print(f"\ntoken sem filtro: {token}\n")
            if not token:
                return jsonify({"erro": "token ausente"}), 401
            try:
                token = token.replace("Bearer ", "") # vai retirar o 'bearer'
                # print(token)
                dados = jwt.decode(token,SECRET_KEY,algorithms=["HS256"])
                # print(dados)
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


except Exception as erro:
    print(f"\n{Alert_Critical("Erro interno")}\nTipo de erro: {Exception}\nErro na:{erro}\nLinha: 41 token")