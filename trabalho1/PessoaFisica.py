from Pessoa import Pessoa
#

class PessoaFisica:
  def __init__(self, cpf: str):
    self.__cpf = cpf

  @property
  def cpf(self):
    return self.__cpf