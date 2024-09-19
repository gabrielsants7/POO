class Pet_virtual:

    def __init__(self, nome): 
        self.nome = nome 
        self.energia = 100

    def comer(self): 
        self.energia += 20

    def brincar(self): 
        self.energia -= 10 
        if self.energia < 0: 
            self.energia = 0

    def dormi(self): 
        self.energia = 100

    def exibir_status(self): 
        return f"{self.nome} tem {self.energia} de energia."