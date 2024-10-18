from veiculo import Veiculo

class Carro(Veiculo):
    
    def __init__(self,marca, modelo, cor, numero_de_portas):
        super().__init__(marca, modelo, cor)
        self.numero_de_portas =  numero_de_portas

    def numero_de_portas(self):
        return self.numero_de_portas


class Motocicleta(Veiculo):

    def __init__(self, marca, modelo, cor, cilindrada, tipo_de_motor):
        super().__init__(marca, modelo, cor)
        self.cilindrada = cilindrada
        self.tipo_de_motor = tipo_de_motor

    def cilindrada(self):
        return self.cilindrada
    
    def tipo_de_motor(self):
        return self.tipo_de_motor