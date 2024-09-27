class Quarto:
    def __init__(self, numero, tipo, disponivel, preço):
        self.numero = numero
        self._tipo = tipo
        self.__disponivel = disponivel
        self.__preço = preço

    def verificar_disponibilidade(self):
        self.__disponivel   


    def obter_tipo(self):
        self._tipo


    def obter_preco(self):
        self.__preço

    def _calcular_preco(self):
        preços = {
            "simples": 90.00,
            "duplo": 170.00,
            "luxo":220.00
        }

    def __alterar_disponibilidade(self, status: bool):
        self.__disponivel = status

    def reservar(self):
        if self.verificar_disponibilidade():
            self.__alterar_disponibilidade(False)
        else:
            print(f"O quarto {self.numero} já está reservado.")
    
    def liberar(self):
        self.__alterar_disponibilidade(True)