from datetime import datetime

from Cliente import Cliente
from Produto import Produto

class NotaFiscal:
    def __init__(self, cliente: Cliente, numero_nota: int, data: datetime, vendedor: str, transportadora: str, impostos: float, produtos_vendidos: [Produto], valor_total: float ):
        self.cliente = cliente
        self.numero_nota = numero_nota
        self.data = data
        self.vendedor = vendedor
        self.transportadora = transportadora
        self.impostos = impostos
        self.produtos_vendidos = produtos_vendidos
        self.valor_total = valor_total