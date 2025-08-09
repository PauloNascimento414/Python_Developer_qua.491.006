import ContaCorrente as cc

def main():
    # instancia do objeto
    conta = cc.ContaCorrente(
        nome="",
        cpf="",
        email="",
        profissao="Suporte de TI",
        telefone="(61) 3301-6575",
        endereco="Qr 414 conj. 11",
        salario=0.0,
        agencia="1010-1",
        numero="10101-1",
        saldo=0.0
    )

    conta.exibir_dados()

if __name__ == "__main__":
    main()