import classes as c
import os

limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

def main():
    # instancia as classes
    usuario = c.PessoaFisica(nome="", cpf="", telefone="", endereco="")
    empresa = c.PessoaJuridica(nome_fantasia="", cnpj="", telefone="", endereco="")

    # input do usuário
    print("Entre com os dados do usuário:\n")

    usuario.nome = input("Informe o Nome: ").strip().title()
    usuario.cpf = input("Informe o CPF: ").strip()
    usuario.telefone = input("Informe o Telefone: ").strip()
    usuario.endereco = input("Informe o Endereço: ").strip().title()

    limpar()

    # input da empresa
    print("Entre com os dados da empresa:\n")

    empresa.nome_fantasia = input("Informe o Nome da Empresa: ").strip().title()
    empresa.cnpj = input("Informe o CNPJ: ").strip()
    empresa.telefone = input("Informe o Telefone da Empresa: ").strip()
    empresa.endereco = input("Informe o Endereço da Empresal: ").strip().title()

    #output
    limpar()
    print("Dados do usuário:")
    usuario.exibir_dados()
    print("Dados da empresa:")
    empresa.exibir_dados()

if __name__ == "__main__":
    main()