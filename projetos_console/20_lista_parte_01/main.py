#lista
nomes = ["Fulano", "Cicrano", "Beltrano", "João", "Maria", "José"]
nomes.sort() #Colocar em ordem alfabetica
nomes.sort(reverse=True) #Colocar em ordem alfabetica inversa de Z a A
#imprime a lista na tela
print(nomes[0])
print(nomes[3])

# imprime o número de itens da lista
print(len(nomes))

for nome in nomes:
    print(nome)