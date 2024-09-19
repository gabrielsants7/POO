class Estudante:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []

    def adicionar_notas(self, notas):
        if len(notas) == 4:
            self.notas = notas
        else:
            print("Erro: Devem ser 4 notas.")

    def obter_media(self):
        return sum(self.notas) / 4


class Turma:
    def __init__(self):
        self.estudantes = {}

    def adicionar_estudante(self, matricula, estudante):
        self.estudantes[matricula] = estudante

    def obter_media_prova(self, numero_prova):
        total = sum(estudante.notas[numero_prova - 1] for estudante in self.estudantes.values())
        return total / len(self.estudantes)
