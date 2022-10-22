class Vendedor:
  def __init__(self, codigo_vendedor: int):
    self.__codigo_vendedor = codigo_vendedor

  @property
  def codigo_vendedor(self):
    return self.__codigo_vendedor