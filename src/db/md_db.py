import bcrypt
from src import SECRET_KEY, Alert_Error, Alert_Success
from flask import jsonify

import jwt
from datetime import datetime, timedelta, timezone

def vrfcr_token(token:str)->dict[str,any]|None:    
    try:
        vldr = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        Alert_Success("Token validado")
        return vldr
    except jwt.ExpiredSignatureError:
        Alert_Error("❌ Token expirado")
        return None
    
    except jwt.InvalidSignatureError:
        Alert_Error("❌ Assinatura inválida")
        return None
    
    except jwt.DecodeError:
        Alert_Error("❌ Erro ao decodificar")
        return None
    
    except jwt.InvalidTokenError as e:
        Alert_Error(f"❌ Erro: {e}")
        return None




def generate_token(email, itr):
    
    now = datetime.now(timezone.utc)
    expiration = now + timedelta(hours=2)
    try:

        body = {
                "id": itr,
                "email": email,
                "role": "DEV",
                "iat": now,
                "exp": expiration
            }
        token = jwt.encode(body, SECRET_KEY, algorithm="HS256")

        vali = vrfcr_token(token)
        # print(f"\ntoke-> {token}\n")
        if vali:
            return token
        else:
            Alert_Error(f"\nToken Inválido\n")
    except Exception as erro:
        Alert_Error(f"\nErro -> {erro}\n")

def generate_hash(senha):
    senha_enco = senha.encode('utf-8')
    salts = bcrypt.gensalt(rounds=12)
    hash_ = bcrypt.hashpw(senha_enco, salts)
    return hash_.decode('utf-8')

def comparador(sn_dgtd, sn_bd ):
    if bcrypt.checkpw(sn_dgtd.encode('utf-8'), sn_bd.encode('utf-8')):
        return True
    else:
        return False

