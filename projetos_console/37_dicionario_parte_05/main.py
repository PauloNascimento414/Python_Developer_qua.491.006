# dicionario

usuario = {
    'nome': "Paulo Henrique",
    'idade': 34,
    'email': "paulo@gmail.com"
}

for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")

# adicionando nova chave
usuario['profissão'] = input("Informe a profissão: ").strip()
print("-"*40)
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")