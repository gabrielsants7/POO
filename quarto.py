class Quarto:
    def __init__(self, numero, tipo, disponivel, preço):
        self.numero = numero
        self._tipo = tipo
        self.__disponivel = True or False
        self.__preço = preço

    def verificar_disponibilidade(self):
        self.__disponivel   


    def obter_tipo(self):
        self._tipo


    def obter_preco(self):
        self.__preço
