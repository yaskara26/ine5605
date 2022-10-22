from PessoaFisica import PessoaFisica


class Cliente:
  def __init__(self, email: str, telefone: str):
    self.__email = email
    self.__telefone = telefone

  @property
  def email(self):
    return self.__email

  @email.setter
  def email(self, email:str):
    self.__email = email

  @property
  def telefone(self):
    return self.__telefone

  @telefone.setter
   def telefone(self, telefone: str):
     self.__telefone = telefone
