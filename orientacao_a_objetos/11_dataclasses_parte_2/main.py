import PessoaFisica
import PessoaJuridica
import os

limpar = lambda: os.system("cls" if os.name == "nt" else "clear")

def main():
    # instancia a classe Pessoa
    pessoafisica = PessoaFisica.PessoaFisica(
        email="",
        telefone="",
        endereco="",
        nome="",  
        cpf="", 
        idade=0,    
    )
    empresa = PessoaJuridica.PessoaJuridica(
        email="", 
        telefone="", 
        endereco="",
        razao_social="",
        nome_fantasia="",
        cnpj=""
    )

    
    # inputs
    print("INFORME OS DADOS DA PESSOA FÍSICA:")
    pessoafisica.nome = input("Informe seu nome: ").strip().title()
    pessoafisica.email = input("Informe seu email: ").strip().lower()
    pessoafisica.telefone = input("Informe seu telefone: ").strip()
    pessoafisica.cpf = input("Informe seu CPF: ").strip()
    pessoafisica.endereco = input("Informe seu Endereço: ").strip()
    pessoafisica.idade = int(input("Informe sua idade: "))

    limpar()

    print("INFORME OS DADOS DA PESSOA JURIDICA:")
    empresa.cnpj = input("Informe o CNPJ da empresa: ")
    empresa.razao_social = input("Informe a Razão Social da empresa: ").strip().title()
    empresa.nome_fantasia = input("Informe o nome da empresa: ").strip().title()
    empresa.email = input("Informe o email da empresa: ").strip().lower()
    empresa.telefone = input("Informe o telefone da empresa: ").strip()
    empresa.endereco = input("Informe o endereço da empresa: ").strip()
    
    

    limpar()

    # output
 
    print(pessoafisica)
    print(empresa)

if __name__ == "__main__":
    main()


