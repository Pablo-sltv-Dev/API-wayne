import bcrypt


def generate_hash(senha):
    
    return bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8') 


# print(generate_hash('senha1234'))
