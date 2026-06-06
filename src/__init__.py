from flask import Flask

# from flask_cors import CORS
from .utils import * #verificao de tipo de usuario e tipo 

try:
    app = Flask(__name__)
    from .config import *
    from .configure import *
    from .routes import *
    
    passe = Verificao().dados_() 

except FileNotFoundError as error:
    print("Erro:", {error}, "\nTipe de Erro: ", {type(error).__name__})
