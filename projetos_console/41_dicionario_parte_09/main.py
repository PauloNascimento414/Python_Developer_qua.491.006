usuarios = [
    {
        'nome': "Paulo",
        'idade': 34,
        'email': "paulo@gmail.com"
    },
    {
        'nome': "Jose",
        'idade': 25,
        'email': "jose@gmail.com"
    },
    {
        'nome': "Maria",
        'idade': 30,
        'email': "maria@gmail.com"
    }
]

#exibe os dados
for usuario in usuarios:
    print("-"*40)
    for chave in usuario:
        print(f"{chave.capitalize()}: {usuario.get(chave)}")