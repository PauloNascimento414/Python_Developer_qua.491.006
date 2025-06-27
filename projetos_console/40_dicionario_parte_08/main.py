chaves = ("Nome", "Idade", "E-mail", "Telefone", "Profissão")
usuario = {
    chaves[0]: "`Paulo Henrique",
    chaves[1]: 34,
    chaves[2]: "paulo@gmail.com",
    chaves[3]: "(61) 9981618-1888",
    chaves[4]: "programador"
}

for chave in chaves:
    print(f"{chave}: {usuario.get(chave)}")
    