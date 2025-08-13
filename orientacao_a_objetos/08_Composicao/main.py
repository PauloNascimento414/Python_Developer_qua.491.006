import classes as c

def main():
    proprietario = c.Pessoa(
        nome="", cpf="", email="",
        telefone="", endereco=""
    )
    carro = c.Veiculo(
        modelo="", fabricante="", cor="",
        placa="", ano="", proprietario=""
    )

    # inputs
    print("DADOS DO PROPRIETÁRIO:")
    proprietario.nome = input("Infome o nome: ").strip().title()
    proprietario.cpf = input("Infome o CPF: ").strip()
    proprietario.email = input("Infome o e-mail: ").strip().lower()
    proprietario.telefone = input("Infome o telefone: ").strip()
    proprietario.endereco = input("Infome o endereço: ").strip().title()

    print("DADOS DO VEÍCULO:")
    carro.modelo = input("Infome o modelo: ").strip().title()
    carro.fabricante = input("Infome o fabricante: ").strip().title()
    carro.cor = input("Infome a cor do carro: ").strip()
    carro.placa = input("Infome a placa do carro: ").strip().upper()
    carro.ano = input("Infome o ano do carro: ").strip()

    carro.proprietario = proprietario

    print("\nExibindo os dados do veículo:\n")
    print(f"Fabricante: {carro.fabricante}")
    print(f"Modelo: {carro.modelo}")
    print(f"Cor: {carro.cor}")
    print(f"Placa: {carro.placa}")
    print(f"Ano: {carro.ano}")
    print(f"Dados do proprietário do veículo: {carro.info_proprietario()}")

if __name__ == "__main__":
    main()