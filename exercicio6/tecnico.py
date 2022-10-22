from pessoa import Pessoa


class Tecnico(Pessoa):
    def __init__(self, nome: str, codigo: int):
        self.__nome = nome
        self.__codigo = codigo