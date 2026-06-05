try:
    from .db import *
except Exception as erro:
    print("\nerro:", erro,'\n')

class User:
    def __init__(self, dados):
        print("\nLinha 5\n",dados,"\n")
        self.user = {
            "email": dados["email"],
            "snh": dados["senha"],
            "tkn": None
        }
        self.email = dados["email"],
        self.snh = dados["senha"],
        self.tkn = None
        # print("\n Linha 10 \n",self.user,"\n")
        
        
    def vrfcr(self):
        print("\nacesso na def veri\n")
        try:
            Rb = Cmds()
            resultado = Rb.verification(self.user)
            # print(f"\nresultado -> {resultado}\n")
            if resultado:
                self.tkn = resultado
                return self.tkn
            else:
                return False

        except Exception as erro:
            return {"Tipo": Exception, "erro": erro}

# teste = User({
    # "email": "teste@gmail.com",
    # "senha": "senha1234"
# })

# print(teste.vrfcr())