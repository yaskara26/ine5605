from locador import Locador
from locatario import Locatario
from mobilia import Mobilia


class Imovel:
    def __init__(self, codigo: int, descricao: str, valor: float, locador: Locador):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__valor = valor
        self.__locador = locador
        self.__locatarios = []
        self.__mobilias = []

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

    @property
    def valor(self):
        return  self.__valor

    @valor.setter
    def valor(self, valor: float):
        self.__valor = valor

    @property
    def locador(self):
        return self.__locador

    @locador.setter
    def locador(self, locador: Locador):
        self.__locador = locador

    @property
    def locatarios(self):
        return self.__locatarios

    def incluir_locatario(self, locatario: Locatario):
        locatario_encontrado = self.find_locatario_by_codigo(locatario.codigo)
        if not locatario_encontrado and isinstance(locatario, Locatario):
            self.__locatarios.append(locatario)

    def excluir_locatario(self, codigo_locatario: int):
        locatario_encontrado = self.find_locatario_by_codigo(codigo_locatario)
        if locatario_encontrado:
            self.__locatarios.remove(locatario_encontrado)

    @property
    def mobilias(self):
        return self.__mobilias

    def incluir_mobilia(self, codigo_mobilia: int, descricao_mobilia: str):
        mobilia_encontrada = self.__find_mobilia_by_codigo(codigo_mobilia)
        if not mobilia_encontrada:
            mobilia = Mobilia(codigo_mobilia, descricao_mobilia)
            self.__mobilias.append(mobilia)

    def excluir_mobilia(self, codigo_mobilia: int):
        mobilia_encontrada = self.__find_mobilia_by_codigo(codigo_mobilia)
        if mobilia_encontrada:
            self.__mobilias.remove(mobilia_encontrada)

    def find_locatario_by_codigo(self, codigo_locatario: int):
        for locatario in self.__locatarios:
            if locatario.codigo == codigo_locatario:
                return locatario

    def __find_mobilia_by_codigo(self, codigo_mobilia: int):
        for mobilia in self.__mobilias:
            if mobilia.codigo == codigo_mobilia:
                return mobilia
