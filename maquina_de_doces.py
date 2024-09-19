class MaquinaDeDoces:
    def __init__(self):
        self.__estoque = 10 # Começamos com 10 doces na máquina

    def exibir_estoque(self):
        print(f"A máquina tem {self.__estoque} doces disponíveis.")

    def vender_doce(self):
        if self.__estoque > 0:
            self.__estoque -= 1
            print("Você comprou um doce! Yum!")
        else:
            print("Desculpe, a máquina está sem doces.")
            
    def reabastecer(self, quantidade):
        if quantidade > 0:
            self.__estoque += quantidade
            print(f"A máquina foi reabastecida com {quantidade} doces.")
        else:
            print("Quantidade inválida para reabastecimento.")