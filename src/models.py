try:
    from .db import *
except Exception as erro:
    print("\nerro:", erro,'\n')

class User:
    def __init__(self, dados):
        self.user = {
            "email": dados["email"],
            "snh": dados["senha"],
            "tkn": None
        }
        self.email = dados["email"],
        self.snh = dados["senha"],
        self.tkn = None
        
        
    def vrfcr(self):
        try:
            Rb = Cmds()
            resultado = Rb.verification(self.user)
            if resultado:
                self.tkn = resultado
                return self.tkn
            else:
                return False

        except Exception as erro:
            return {"Tipo": Exception, "erro": erro}
