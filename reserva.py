from datetime import date
class Reserva:
    def __init__(self, quarto, quantidade_diarias, check_in, check_out):
        self._quarto = quarto
        self._quantidade_diarias = quantidade_diarias
        self.__check_in = check_in
        self.__check_out = check_out

    def obter_periodo(self):
        return self.__check_in, self.__check_out

    def _calcular_valor(self):
        return  self._quarto.obter_preco() * self._quantidade_diarias