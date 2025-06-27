usuario = dict(
    nome="Paulo Henrique", 
    idade=34, 
    email="paulo@gmail.com"
)

for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")