#dicionário
usuario = {
    'nome': "Paulo Henrique",
    'idade': 34,
    'email': "paulo@gmail.com",
    'profissão': "programador"
}

for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")