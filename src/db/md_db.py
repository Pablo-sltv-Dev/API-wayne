import bcrypt
from src import SECRET_KEY
from flask import jsonify

import jwt
from datetime import datetime, timedelta, timezone

def vrfcr_token(token:str)->dict[str,any]|None:    
    try:
        vldr = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        print(f"vldr -> {vldr}")
        return vldr
    except jwt.ExpiredSignatureError:
        print("❌ Token expirado")
        return None
    
    except jwt.InvalidSignatureError:
        print("❌ Assinatura inválida")
        return None
    
    except jwt.DecodeError:
        print("❌ Erro ao decodificar")
        return None
    
    except jwt.InvalidTokenError as e:
        print(f"❌ Erro: {e}")
        return None




def generate_token(email, itr):
    print("gerador acessado")
    
    now = datetime.now(timezone.utc)
    expiration = now + timedelta(hours=2)
    print("NOW:", now)
    print("EXP:", expiration)
    try:

        print(f"\nemail: {email}\nid:{itr}\n{SECRET_KEY}\n")
        body = {
                "id": itr,
                "email": email,
                "role": "DEV",
                "iat": now,
                "exp": expiration
            }
        print(body,"\n")
        token = jwt.encode(body, SECRET_KEY, algorithm="HS256")

        vali = vrfcr_token(token)
        # print(f"\ntoke-> {token}\n")
        print(f"\nValidação de token: {vali}\n")
        if vali:
            print(f"\nValidação de token: validou\n{vali}")
            return token
        else:
            print(f"\nToken Inválido\n")
    except Exception as erro:
        print(f"\nErro -> {erro}\n")

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

