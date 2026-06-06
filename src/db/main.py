import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv, dotenv_values
import os
from .md_db import comparador, generate_token, vrfcr_token
from src import Alert_Error, Alert_Success




def snh_hash(senha):
        return senha.decode()
    




class Cnx:
    def __init__(self):
        
        load_dotenv()
        try:
            config = {
                "user":str(os.getenv("API_USER")),
                "password": str(os.getenv("API_PASSOWRD")) ,
                "host": str(os.getenv("API_HOST")) ,
                "database": str(os.getenv("API_DB")) ,
            }

            self.conexao = mysql.connector.connect(**config)
           
            Alert_Success("Cnx validado")
            return 
        except Error as e:
            Alert_Error("Erro ao conectar ao MySQL COnnector")
            return None
    
    def teste(self):
        if self.conexao.is_connected():
            print("\n__CONECTADO AO BANCO DE DADOS__\n")
            self.conexao.close()
            return True
        else:
            return False


class CrS(Cnx):
    def __init__(self):
        super().__init__()
        try:
            self.cursor = self.conexao.cursor(dictionary=True)
            return 
        except Error as erro:
            Alert_Error("Erro ao conectar ao MySQL COnnector")


    def Vizualizar_table(self):
        try:

            query = 'SELECT * FROM EmployeeS;'
            self.cursor.execute(query)
            resultado = self.cursor.fetchall()
            print("\n", resultado, "\n")
            self.cursor.close()
            self.conexao.close()
            return resultado[0]
        except Error as error:
            print("\n", error)


    


class Cmds(CrS):
    def __init__(self):
        super().__init__()
    
    def verification(self, dados):
        try:

            self.cursor.execute('SELECT ID_cntt,SNH_cntt FROM CNTS WHERE EMAIL_cntt = %s', (dados['email'],)) # verifica se o email registrado é o mesmo email enviado


            resultado = self.cursor.fetchone() # Aqui retorna o resultado da query
            if resultado:
                sn_str = resultado['SNH_cntt'] # obj -> str
                if comparador(dados['snh'], sn_str):
                    ml = dados['email']
                    gerador = generate_token(ml, resultado['ID_cntt'])
                    return gerador
                else:
                    return False
            else:
                return False
            
        except Exception as erro:
            Alert_Error("Erro ao conectar ao MySQL COnnector")


    


