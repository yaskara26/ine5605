from TelaCliente import TelaCliente
from Cliente import Cliente

class ControladorCliente:
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_cliente = TelaCliente()
        self.__clientes = []

    def inclui_cliente(self):
        dados_cliente = self.__tela_cliente.pega_dados_cliente()
        cliente = Cliente(dados_cliente["nome_cliente"],
                          dados_cliente["telefone_cliente"])
        if not self.retorna_cliente_pelo_nome(cliente.nome):
            self.__clientes.append(cliente)

    def retorna_cliente_pelo_nome(self, nome):
        for cliente in self.__clientes:
            if cliente.nome == nome:
                return cliente
