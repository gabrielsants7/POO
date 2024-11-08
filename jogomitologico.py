import random

class criatura:
    def __init__(self, nome, tipo, habitat, força, resistencia, dano):
        self.nome = nome
        self.tipo = tipo
        self.habitat = habitat
        self.força = força
        self.resistencia = resistencia
        self.dano = dano
        self.vida = 200

    def atacar(self, outra_criatura):
        dano_causado = self.dano

        if self.habitat == batalha.cenario:
            aumento_resistencia = self.resistencia * 0.2
            self.resistencia += aumento_resistencia
            print(f"{self.nome} tem sua resistência aumentada em {aumento_resistencia:.2f}%. Nova resistência {self.resistencia:.2f}")

            diminuicao_resistencia = outra_criatura.resistencia * 0.1
            outra_criatura.resistencia -= diminuicao_resistencia
            print(f"{outra_criatura.nome} tem sua resistência diminuída em {diminuicao_resistencia:.2f}. Nova resistência: {outra_criatura.resistencia:.2f}")

      outra_criatura.receber_dano(dano_causado)   

    def receber_dano(self, dano):
        dano_reduzido