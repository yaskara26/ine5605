from abstractElevador import AbstractElevador
from elevadorCheioException import ElevadorCheioException
from elevadorJahNoTerreoException import ElevadorJahNoTerreoException
from elevadorJahNoUltimoAndarException import ElevadorJahNoUltimoAndarException
from elevadorJahVazioException import ElevadorJahVazioException


class Elevador(AbstractElevador):
    def __init__(self, capacidade: int, total_pessoas: int, total_andares: int, andar_atual):
        self.__capacidade = capacidade
        self.__total_pessoas = total_pessoas
        self.__total_andares_predio = total_andares
        self.__andar_atual = andar_atual

    # ElevadorJahNoTerreoException
    def descer(self) -> str:
        if self.__andar_atual == 0:
            raise ElevadorJahNoTerreoException
        else:
            self.__andar_atual -= 1

    # ElevadorCheioException
    def entra_pessoa(self) -> str:
        if self.__capacidade == self.__total_pessoas:
            raise ElevadorCheioException
        else:
            self.__total_pessoas += 1

    # ElevadorJahVazioException
    def sai_pessoa(self) -> str:
        if self.__total_pessoas == 0:
            raise ElevadorJahVazioException
        else:
            self.__total_pessoas -= 1

    # ElevadorJahNoUltimoAndarException
    def subir(self) -> str:
        if self.__andar_atual == self.__total_andares_predio:
            raise ElevadorJahNoUltimoAndarException
        else:
            self.__andar_atual += 1

    @property
    def capacidade(self) -> int:
        return self.__capacidade

    @property
    def total_pessoas(self) -> int:
        return  self.__total_pessoas

    @property
    def total_andares_predio(self) -> int:
        return self.__total_andares_predio

    @property
    def andar_atual(self) -> int:
        return self.__andar_atual

    @total_andares_predio.setter
    def total_andares_predio(self, total_andares_predio: int):
        self.__total_andares_predio = total_andares_predio
