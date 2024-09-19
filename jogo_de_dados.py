import random

class JogoDeDados: 
    def __init__(self, jogador1, jogador2):

        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.resultado1 = 0
        self.resultado2 = 0

    def rolar_dados(self):
        self.resultado1 = random.randint(1, 6)
        self.resultado2 = random.randint(1, 6)
        print(f'{self.jogador1} rolou {self.resultado1}')
        print(f'{self.jogador2} rolou {self.resultado2}')

    def determinar_vencedor(self):
        if self.resultado1 > self.resultado2:
            return f'{self.jogador1} venceu com {self.resultado1} contra {self.resultado2}!'
        elif self.resultado2 > self.resultado1:
            return f'{self.jogador2} venceu com {self.resultado2} contra {self.resultado1}'
        else:
            return 'Empate! Ambos os jogadores rolaram o mesmo número'
    
    