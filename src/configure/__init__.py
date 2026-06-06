try:
    from .decorates import *
    from ..utils import Alert_Critical
except Exception as erro:
    print(f"\n{Alert_Critical("Erro interno")}\nTipo de erro: {Exception}\nErro na:{erro}\n")