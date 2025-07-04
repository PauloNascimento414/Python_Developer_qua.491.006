import json
import os

pessoa = {}

try:
    arquivo = input("Informe o nome do arquivo: ").strip().lower()

    with open(f"{arquivo}.json", "r",encoding="utf-8") as f:
        pessoas = json.load(f)

    # usuário informa os dados da nova pessoa
    pessoa['nome'] = input("Informe o nome: ").title().strip()
    pessoa['idade'] = int(input("Inofme a idade: "))
    pessoa['cpf'] = input("Informe o CPF: ").strip()
    pessoa['rg'] = input("Informe o RG: ").strip()
    pessoa['data_nasc'] = input("Informe a Data de Nascimento: ").strip()
    pessoa['sexo'] = input("Informe o gênero: ").strip()
    pessoa['signo'] = input("Informe o signo: ").strip().capitalize()
    pessoa['mae'] = input("Informe o nome da mâe: ").title().strip()
    pessoa['pai'] = input("Informe o nome do pai: ").title().strip()
    pessoa['email'] = input("Informe o e-mail: ").lower().strip()
    pessoa['senha'] = input("Informe a senha: ")
    pessoa['cep'] = input("Informe o CEP: ").strip()
    pessoa['endereco'] = input("Informe o endereço: ").title().strip()
    pessoa['numero'] = input("Informe o número do endereço: ")
    pessoa['bairro'] = input("Informe o bairro: ").capitalize().strip()
    pessoa['cidade'] = input("Informe a cidade: ").title().strip()
    pessoa['estado'] = input("Informe a estado: ").upper().strip()
    pessoa['telefone_fixo'] = input("Informe o telefone: ").strip()
    pessoa['celular'] = input("Informe o celular: ").strip()
    pessoa['altura'] = float(input("Informe a altura: ").replace(",", "."))
    pessoa['peso'] = float(input("Informe o peso: ").replace(",", "."))
    pessoa['tipo_sanguineo'] = input("Informe o tipo sanguíneo: ").upper().strip()
    pessoa['cor'] = input("Informe a cor: ").strip()

    pessoas.append(pessoa)

    with open(f"{arquivo}.json", "w", encoding="utf-8") as f:
        json.dump(pessoas,f, ensure_ascii=False, indent=4)

    with open(f"{arquivo}.json", "r", encoding="utf-8") as f:
        pessoas = json.load(f)

    print(f"{'-'*20} LISTA DE PESSOAS {'-'*20}")
    for pessoa in pessoas:
        for chave in pessoa:
            print(f"{chave.capitalize()}: {pessoa.get(chave)}")
        print('-'*40)
except Exception as e:
    print(f"Não foi possível inserir pessoa. {e}.")