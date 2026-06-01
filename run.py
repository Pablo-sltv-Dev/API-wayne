from src import app, passe

try:

    if __name__ == '__main__':
        # app.run(debug=True)
        if passe:
            app.run(
                host='0.0.0.0',
                port=passe['PORT'],
                debug=passe['DEBUG']

            )
            
except NameError as erro: #variable
    print("Error:", NameError, "\nTipo de erro: ", {type(erro).__name__})

except FileNotFoundError as erro:
    print("Error:", FileNotFoundError, "\nTipo de erro: ", {type(erro).__name__})
except IndentationError as erro:
    print("Error:", IndentationError, "\nTipo de erro: ", {type(erro).__name__})
    