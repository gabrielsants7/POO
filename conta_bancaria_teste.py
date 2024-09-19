from conta_bancaria import ContaBancaria

conta_gabriel = ContaBancaria("Gabriel", 100)

print(f"Saldo inicial de {conta_gabriel.get_titular()}: R${conta_gabriel.get_saldo():.2f}")

conta_gabriel.depositar(50)
conta_gabriel.sacar(30)
conta_gabriel.sacar(150)

print(f"Saldo final de {conta_gabriel.get_titular()}: R${conta_gabriel.get_saldo():.2f}")

conta_gabriel.set_titular("Gabriel Santos")
print(f"Novo titular da conta: {conta_gabriel.get_titular()}")