from Cliente import Cliente
from CategoriaProduto import CategoriaProduto


class Produto:

    def __init__(self, codigo: int, descricao: str, categoria_produto: CategoriaProduto):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__categoria_produto = categoria_produto
        self.__quantidade = None
        self.__preco_unitario = None
        self.__cliente = None

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo
  
    @property
    def descricao(self) -> int:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

    @property
    def categoria_produto(self) -> str:
        return self.__categoria_produto

    @categoria_produto.setter
    def categoria_produto(self, categoria_produto: str):
        self.__categoria_produto = categoria_produto

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade

    @property
    def preco_unitario(self):
        return self.__preco_unitario

    @preco_unitario.setter
    def preco_unitario(self, preco_unitario):
        self.__preco_unitario = preco_unitario

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente: Cliente):
        self.__cliente = cliente

    def preco_total(self):
        return self.preco_unitario * self.quantidade
