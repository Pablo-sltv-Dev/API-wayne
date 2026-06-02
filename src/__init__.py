from flask import Flask
from flask_cors import CORS
from .utils import * #verificao de tipo de usuario e tipo de porta
from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()

app = Flask(__name__)
SECRET_KEY=os.getenv("SECRET_KEY")


CORS(app, resources={ # aqui permite qual url pode acessar
    r"/rta/*":{
        "origins": ["https://solotv-3391511.postman.co/workspace/Final-Project-Infinity~9360ac56-9360-4842-b265-15c6250018a6/request/47017727-31766f6b-7b18-4299-863f-2130fa482d06?action=share&creator=47017727"],
        "methods":["GET", "POST"],
        "allow_header": ["Content-Type"]
    }
})

try:
    from .routes import *
    
    passe = Verificao().dados_() 

except FileNotFoundError as error:
    print("Erro:", {error}, "\nTipe de Erro: ", {type(error).__name__})
