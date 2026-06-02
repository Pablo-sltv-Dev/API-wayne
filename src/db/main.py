import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv, dotenv_values
import os
import bcrypt
import jwt
from datetime import datetime, timedelta


def generate_hash(senha):
    
        return bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()) 

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
        super().__init__()
    
    def verification(self, dados):

        self.cursor.execute('SELECT ID_cntt,SNH_cntt FROM CNTS WHERE EMAIL_cntt = %s', (dados['email'],)) # verifica se o email registrado é o mesmo email enviado

        resultado = self.cursor.fetchone() # Aqui retorna a senha
        swww = resultado['SNH_cntt'] # transforma obj em str
        # print("\nteste:",swww,"\n")


        

        # print(bool(consulta))

        if bcrypt.checkpw(dados['snh'].encode('utf-8'),swww.encode('utf-8')): # faz a comparação
            k = jwt.encode(
                {
                    "id":resultado['ID_cntt'],
                    "email": dados['email'],
                    "exp": datetime.now() + timedelta(hours=2)

                },
                os.getenv("SECRET_KEY"),
                algorithm="HS256"
            )
            
            return k
        else:
            return False
        
# teste = Cmds()

# print(teste.verification("teste@gmail.com", {"senha":"senha1234"}))
