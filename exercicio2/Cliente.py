class Cliente:
    def __init__(self, cpf: int, nome: str, endereco: str, email: str, telefone: str):
        self.cpf = cpf
        self.nome = nome
        self.endereco = endereco
        self.email = email
        self.telefone = telefone
    
    def __str__(self):
        return f'Cliente({self.cpf}, {self.nome}, {self.endereco}, {self.email}, {self.telefone})'