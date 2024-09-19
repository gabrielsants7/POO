from jogo_de_dados import JogoDeDados


#Criando uma instancia do jogo com dois jogadores 
jogo= JogoDeDados ("Alice", "Bob")

#Rolando os dados 
jogo.rolar_dados()

# Determinando e exibindo o vencedor 
vencedor = jogo.determinar_vencedor()
print(vencedor)

