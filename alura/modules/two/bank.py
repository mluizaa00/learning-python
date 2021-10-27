import uuid;

def create_account(name, cpf, income):
    account = {
        "id": uuid.uuid1(),
        "name": name,
        "cpf": cpf,
        "income": income
    };
    
    return account;