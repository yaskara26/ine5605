"""Universidade Federal de Santa Catarina.
   CTC - Centro Tecnologico - http://ctc.ufsc.br
   INE - Departamento de Informatica e Estatistica - http://inf.ufsc.br
"""

class Ordenacao():

    def __init__(self, array_para_ordenar:[]):
        """Recebe o array com o conteudo a ser ordenado"""
        ...
        self.array_para_ordenar = array_para_ordenar

    def ordena(self):
        """Realiza a ordenacao do conteudo do array recebido no construtor"""
        ...
        
        self.ordena_bolha()

    def ordena_bolha(self):
        tamanho_lista = len(self.array_para_ordenar)
        for j in range(tamanho_lista):
            for i in range(1, tamanho_lista - j):
                elemento_anterior = self.array_para_ordenar[i - 1]
                elemento_atual = self.array_para_ordenar[i]
                if elemento_anterior > elemento_atual:
                    self.trocar(self.array_para_ordenar, i, i - 1)

    def trocar(self, lista, posicao_a, posicao_b):
        """swap"""
        temporario = lista[posicao_a]
        lista[posicao_a] = lista[posicao_b]
        lista[posicao_b] = temporario
        
    def toString(self):
        """Converte o conteudo do array em String formatado
           Exemplo: 
           Para o conteudo do array: [1,2,3,4,5]
           Retorna: "1,2,3,4,5"
           @return String com o conteudo do array formatado
     """
        string_list = list(map(str, self.array_para_ordenar))
        
        return ','.join(string_list)