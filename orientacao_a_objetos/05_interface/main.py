import classes as c

def main():
    # instancia objeto da classe Conta
    cc  = c.ContaCorrente(
        titular="", 
        cpf="", 
        agencia="",
        conta="",
        saldo=0.0
    )

    print(f"Saldo: R$ {cc.saldo}")

if __name__ == "__main__":
    main()
