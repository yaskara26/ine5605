from datetime import datetime

class Loja:
    def __init__(self):
        self.clientes: [Cliente] = []
        self.vendedores: [str] = []
        self.notas_fiscais: [NotaFiscal] = []
    
    def buscar_vendas_no_periodo(self, data_inicial: datetime, data_final: datetime):
        pass
    
    def calcular_vendas_do_vendedor_no_periodo(self, vendedor, data_inicial: datetime, data_final: datetime):
        pass