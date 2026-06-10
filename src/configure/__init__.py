try:
    from .decorates import *
    from ..utils import Alert_Critical
    from .vr_token import *
except Exception as erro:
    print(f"\n{Alert_Critical("Erro interno")}\nTipo de erro: {Exception}\nErro: {erro}\nLinha 6")