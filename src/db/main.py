import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv, dotenv_values
import os
from .md_db import comparador, generate_token, vrfcr_token





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
           
            return 
        except Error as e:
            print("\nErro ao conectar ao MySQL COnnector: ", e)
            return None
    
    def teste(self):
        if self.conexao.is_connected():
            print("\n__CONECTADO AO BANCO DE DADOS__\n")
            self.conexao.close()
            return True


class CrS(Cnx):
    def __init__(self):
        super().__init__()
        try:
            self.cursor = self.conexao.cursor(dictionary=True)
            return 
        except Error as erro:
            print("\nTipo:", erro)


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
        print("\nclass db acessado\n")
        super().__init__()
    
    def verification(self, dados):
        print("\nmetodo veri acessado\n")
        try:

            self.cursor.execute('SELECT ID_cntt,SNH_cntt FROM CNTS WHERE EMAIL_cntt = %s', (dados['email'],)) # verifica se o email registrado é o mesmo email enviado


            resultado = self.cursor.fetchone() # Aqui retorna o resultado da query
            if resultado:
                sn_str = resultado['SNH_cntt'] # obj -> str
                if comparador(dados['snh'], sn_str):
                    print("\nSenha Aprovada\n")
                    ml = dados['email']
                    gerador = generate_token(ml, resultado['ID_cntt'])
                    return gerador
                else:
                    return False
            else:
                return False
            
        except Exception as erro:
            print(f"\nErro: {erro}\n")

    


