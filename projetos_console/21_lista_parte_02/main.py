#lista
nomes = [
    "Alex",
    "Joana",
    "João",
    "Mariana",
    "Mário",
    "Fernanda"
]

#exibe a lista

for nome in nomes:
    print(nome)

# usuário informa nome a ser acrescetada na lista
novo_nome = input("Informe o novo nome: ").title().strip()

# novo nome é inserido na lista
nomes.append(novo_nome)

# re-exibir a lista
for nome in nomes:
    print(nome)