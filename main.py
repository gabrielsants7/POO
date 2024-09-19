from maquina_de_doces import MaquinaDeDoces

# Criando uma instância da máquina de doces
maquina = MaquinaDeDoces()

# Exibindo o estoque inicial
maquina.exibir_estoque()

# Vendendo alguns doces
maquina.vender_doce()
maquina.vender_doce()

# Exibindo o estoque após algumas vendas
maquina.exibir_estoque()

# Reabastecendo a máquina
maquina.reabastecer(5)

# Exibindo o estoque final
maquina.exibir_estoque()