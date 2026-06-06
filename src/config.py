from src import app
from flask import jsonify
# from flask import Flask
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv, dotenv_values
import os, logging
try:
    CORS(app,resources={ # aqui permite qual url pode acessar
        # http://127.0.0.1:5500/index.html
        r"/rta/*": {
            "origins": ["http://localhost:5500","http://127.0.0.1:5500"],
            "methods":["GET", "POST"],
            "allow_header": ["Content-Type"]
        }
    })

    load_dotenv()

    SECRET_KEY=os.getenv("SECRET_KEY")

    #_________________________
    limiter = Limiter(
        key_func= get_remote_address, #identificar por ip
        app=app,
        default_limits=['8 per minute']
    )
    #_______________________
    logger = app.logger
except Exception as erro:
    print({"menssage": "algo deu errado", "Error": erro})



