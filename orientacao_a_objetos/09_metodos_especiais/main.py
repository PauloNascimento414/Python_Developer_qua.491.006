import Pessoa

def main():
    usuario = Pessoa.Pessoa(nome="Paulo", idade=34)

    print(usuario)
    print(f"Idade: {len(usuario)}")

    # destruição do objeto
    del(usuario)

    

if __name__ == "__main__":
    main()