from animal import Animal, abstractmethod


class Ave(Animal):
    @abstractmethod
    def __init__(self, tamanho_passo: int, altura_voo: int):
        super().__init__(tamanho_passo)
        self.__altura_voo = altura_voo

    @property
    def altura_voo(self):
        return self.__altura_voo

    @altura_voo.setter
    def altura_voo(self, altura_voo: int):
        self.__altura_voo = altura_voo

    def mover(self):
        return super().mover() + ' VOANDO'

    @abstractmethod
    def produzir_som(self):
        return 'AVE: PRODUZ SOM: '
