try:
    from ..utils import Alert_Critical
    from .route import *
except Exception as erro:
    print(f"\n{Alert_Critical("Erro interno")}\nTipo de erro: {Exception}\nErro na:{erro}\n")
