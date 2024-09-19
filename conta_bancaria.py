class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.__titular = titular
        self.__saldo = saldo_inicial
    def get_saldo(self):
        return self.__saldo
    def depositar(self, valor1):
        self.valor1 = valor1
        
    def sacar(self, valor2):
        self.valor2 = valor2
        if valor2 > self.__saldo:
            print('Seu saldo é insuficiente!')
    def set_titular(self, novo_titular):
        self.novo_titular = novo_titular
    def get_titular(self):
        return self.__titular
