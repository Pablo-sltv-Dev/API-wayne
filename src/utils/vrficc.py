from dotenv import load_dotenv
import os

class Verificao:
   
    
    def __init__(self):
        load_dotenv()
        try:
            self.Tipo = os.getenv("FLASK_DEV_ENV")
            
            if self.Tipo == 'development':
                self.dados = {
                    "TIPO" : os.getenv("FLASK_DEV_ENV"),
                    "DEBUG": os.getenv("FLASK_DEV_DEBUG"),
                    "PORT": os.getenv("FLASK_DEV_PORT")
                    }

                
            elif self.Tipo == "industri":
                print("ainda nao fiz")
           
 
            # print(self.dados)
            # print(self.Tipo)
        except KeyError as error:
            print("Error: ", {error}, "\nType Error: ", {type(error).__name__})
            return False
            
    def dados_(self):
        return self.dados





