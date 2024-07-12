import re

def validar_email(email):
    
    padrao = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(padrao, email))


def validar_nome(nome):
    # Esta função verifica se o nome contém apenas letras e espaços
    if nome.replace(" ", "").isalpha():
        return True
    else:
        print("Nome inválido. Por favor, insira apenas letras e espaços.")
        return False
    
def validar_endereço(endereço):
    # Esta função verifica se o nome contém apenas letras e espaços
    if endereço.replace(" ", "").isalpha():
        return True
    else:
        print("Endereço inválido. Por favor, insira apenas letras e espaços.")
        return False
    
def validar_telefone(telefone):
   
    padrao = r'^\d{4,5}-\d{4}$'
    if re.match(padrao, telefone):
        return True
    else:
        return False   
