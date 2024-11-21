import random

class Criatura:
    def __init__(self, nome, tipo, habitat, vida, forca, resistencia, dano, magia_veneno, magia_gelo, item):
        self.nome = nome
        self.tipo = tipo
        self.habitat = habitat
        self.vida = vida
        self.forca = forca
        self.resistencia = resistencia
        self.dano = dano
        self.magia_veneno = magia_veneno
        self.magia_gelo = magia_gelo
        self.item = item
        self.veneno = 0  
        self.gelo = 0   

    def ataque(self, outro):
        dano_final = self.dano
        if outro.gelo > 0:
            dano_final = dano_final * (1 - outro.gelo)
        dano_final -= outro.resistencia * 0.1
        if dano_final < 0:
            dano_final = 0
        outro.vida -= dano_final
        return dano_final

    def usar_magia_veneno(self, outro):
        outro.vida -= self.magia_veneno
        outro.veneno += 1
        return self.magia_veneno

    def usar_magia_gelo(self, outro):
        outro.gelo = 0.1 
        return "Gelo lançado!"

    def usar_item(self):
        if self.item == "Elixir de Cura":
            cura = 20
            self.vida += cura
            return f"{self.nome} usou Elixir de Cura e restaurou {cura} de vida!"
        elif self.item == "Armadura Mágica":
            self.resistencia += 10
            return f"{self.nome} usou Armadura Mágica, aumentando sua resistência!"

    def esta_vivo(self):
        return self.vida > 0

def batalha(criatura1, criatura2):
    turnos = 1
    while criatura1.esta_vivo() and criatura2.esta_vivo():
        print(f"\n--- Turno {turnos} ---")
        if random.choice([True, False]):
            atacante, defensor = criatura1, criatura2
        else:
            atacante, defensor = criatura2, criatura1

        print(f"{atacante.nome} está atacando!")

        print("Escolha uma ação:")
        print("1. Atacar")
        print("2. Usar Magia de Veneno")
        print("3. Usar Magia de Gelo")
        print("4. Usar Item")
        print("5. Passar o turno")

        escolha = int(input(f"O que {atacante.nome} vai fazer? (1-5): "))

        if escolha == 1:
            dano = atacante.ataque(defensor)
            print(f"{atacante.nome} atacou! Causou {dano} de dano!")
        elif escolha == 2:
            dano_veneno = atacante.usar_magia_veneno(defensor)
            print(f"{atacante.nome} usou Veneno! Causou {dano_veneno} de dano ao longo do tempo!")
        elif escolha == 3:
            efeito_gelo = atacante.usar_magia_gelo(defensor)
            print(f"{atacante.nome} usou Gelo! {efeito_gelo}")
        elif escolha == 4:
            efeito_item = atacante.usar_item()
            print(efeito_item)
        elif escolha == 5:
            print(f"{atacante.nome} passou o turno.")

        print(f"{criatura1.nome} tem {criatura1.vida} de vida.")
        print(f"{criatura2.nome} tem {criatura2.vida} de vida.")

        turnos += 1

    if criatura1.esta_vivo():
        print(f"{criatura1.nome} venceu a batalha!")
    else:
        print(f"{criatura2.nome} venceu a batalha!")

fenix = Criatura("Fênix", "Mítica", "Floresta", 200, 50, 30, 15, 5, "Gelo", "Elixir de Cura")
minotauro = Criatura("Minotauro", "Mítica", "Labirinto", 200, 60, 40, 20, 5, "Gelo", "Armadura Mágica")

batalha(fenix, minotauro)