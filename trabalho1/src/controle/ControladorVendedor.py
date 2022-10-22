from TelaVendedor import TelaVendedor
from Vendedor import Vendedor


class ControladorVendedor:
  def __init__(self, controlador_principal):
    self.__controlador_principal = controlador_principal
    self.__tela_vendedor = TelaVendedor()
    self.__vendedor = []

  def inclui_vendedor(self):
    dados_vendedor = self.__tela_vendedor.pega_dados_vendedor()