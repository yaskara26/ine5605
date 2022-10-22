from imovel import Imovel


class Imobiliaria:
    def __init__(self):
        self.__imoveis = []

    @property
    def imoveis(self):
        return self.__imoveis

    def incluir_imovel(self, imovel: Imovel):
        if not imovel:
            return

        imovel_encontrado = self.__find_imovel_by_codigo(imovel.codigo)
        if not imovel_encontrado and isinstance(imovel, Imovel):
            self.__imoveis.append(imovel)

    def excluir_imovel(self, imovel: Imovel):
        if not imovel:
            return

        imovel_encontrado = self.__find_imovel_by_codigo(imovel.codigo)
        if imovel_encontrado:
            self.__imoveis.remove(imovel_encontrado)

    def __find_imovel_by_codigo(self, codigo_imovel: int):
        for imovel in self.__imoveis:
            if imovel.codigo == codigo_imovel:
                return imovel
