import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv, dotenv_values
import os

teste = str

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


# try:
#     teste = CrS()
#     dados = teste.Vizualizar_table()

#     for dado in dados:
#         print("\n", dado,"\n")

# except TypeError as erro:
#     print("\nerro:", TypeError, "\nTipo: ", erro)