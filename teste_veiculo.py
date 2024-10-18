from veiculo import Veiculo
from motocarro import Carro
from motocarro import Motocicleta

carro = Veiculo("Wolkswagen", "Gol", "Vermelho")

motocicleta = Veiculo("Honda", "XRE", "Preta")

print(  carro.marca)
print(carro.modelo)
print(carro.cor)
print(motocicleta.marca)
print(motocicleta.modelo)
print(motocicleta.cor)