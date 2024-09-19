from pet_virtual import Pet_virtual
# criando uma instâcia do pet pet Pet_virtual("nani")
pet = Pet_virtual('nani')

# Interagindo com o pet
pet.comer() # 0 pet come e ganha energia
print(f"{pet.nome} comeu e agora tem {pet.energia} de energia!!!")

pet.brincar() # 0 pet brinca e perde energia
print(f"{pet.nome} brincou e agora tem {pet.energia} de energia!!!")
pet.dormi() # 0 pet dorme e sua energia é restaurada print(F"{pet.nome} dormiu e agora tem {pet.energia} de energia!!")

#exibindo o status final do pet print(pet.exibir_status())
print(pet.exibir_status())