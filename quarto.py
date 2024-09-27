class Quarto:
    def __init__(self, numero, tipo):
        self.numero = numero
        self._tipo = tipo
        self.__disponivel = True
        self.__preço = self._calcular_preco()  


    def verificar_disponibilidade(self):
        return self.__disponivel   


    def obter_tipo(self):
        return self._tipo


    def obter_preco(self):
        return self.__preço


    def _calcular_preco(self):
        preços = {
            "simples": 90.00,
            "duplo": 170.00,
            "luxo": 220.00
        }
        return preços.get(self._tipo.lower(), 90.00)


    def __alterar_disponibilidade(self, status: bool):
        self.__disponivel = status


    def reservar(self):
        if self.verificar_disponibilidade():
            self.__alterar_disponibilidade(False)
        else:
            print(f"O quarto de número {self.numero} já foi reservado!")
    

    def liberar(self):
        self.__alterar_disponibilidade(True)


