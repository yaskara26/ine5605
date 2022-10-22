from abstractControladorElevador import AbstractControladorElevador
from comandoInvalidoException import ComandoInvalidoException
from elevador import Elevador


class ControladorElevador(AbstractControladorElevador):
    def __init__(self):
        self.__elevador = None

    def subir(self) -> str:
        self.__elevador.subir()

    def descer(self) -> str:
        self.__elevador.descer()

    def entra_pessoa(self) -> str:
        self.__elevador.entra_pessoa()

    def sai_pessoa(self) -> str:
        self.__elevador.sai_pessoa()

    @property
    def elevador(self) -> Elevador:
        return self.__elevador

    def inicializar_elevador(self,
                             andar_atual: int,
                             total_andares_predio: int,
                             capacidade: int,
                             total_pessoas: int):
        todos_sao_inteiros = isinstance(andar_atual, int) \
                             and isinstance(total_andares_predio, int) \
                             and isinstance(capacidade, int) \
                             and isinstance(total_pessoas, int)

        if not todos_sao_inteiros:
            raise ComandoInvalidoException

        todos_sao_positivos = capacidade >= 0 \
                              and total_andares_predio >= 0 \
                              and andar_atual >= 0 \
                              and total_pessoas >= 0

        if not todos_sao_positivos:
            raise ComandoInvalidoException

        andar_atual_eh_valido = andar_atual <= total_andares_predio
        total_pessoas_eh_valido = total_pessoas <= capacidade
        if not andar_atual_eh_valido or not total_pessoas_eh_valido:
            raise ComandoInvalidoException

        self.__elevador = Elevador(capacidade,
                                   total_pessoas,
                                   total_andares_predio, andar_atual)
