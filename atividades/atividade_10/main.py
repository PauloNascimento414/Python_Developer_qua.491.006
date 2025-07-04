"""
#TODO - atividade: faça um CRUD (Create, Read, Update, Delete) em um JSON.
Opções do menu:
- Criar um novo arquivo JSON (usuário irá informar o diretório).
- Abrir arquivo JSON (usuário irá informar o diretório).
- Cadastrar novo usuário em um JSON.
- Listar todos os usuários de um arquivo JSON.
- Pesquisar usuário através do valor de uma chave em um arquivo JSON.
- Alterar dados de um usuário em um arquivo JSON.
- Deletar usuário de um arquivo JSON.
- Sair do programa
Dados do usuário:
- Nome
- Data de nascimento
- CPF
- E-mail
- Filme favorito do usuário
#NOTE - Mostre o nome do arquivo eo diretório no menu
"""

import json
import os

#lista
usuarios = []

while True:
    #dicionario
    usuario = {}
    # menu
    print(f"{'-'*20} Menu {'-'*20}")
    print("1 - Criar um novo arquivo JSON.")
    print("2 - Abrir arquivo JSON.")
    
    opcao = input("Informe a opção desejada: ")

    match opcao:
        case "1":
            try:
                novo_arquivo = input("Iforme o nome do arquivo: ").strip().lower()
                diretorio = input("Iforme o diretorio do arquivo: ").strip().lower()
                
                with open(f"{diretorio}/{novo_arquivo}.json", "w", encoding="utf-8") as f:
                    json.dump(usuarios, f, ensure_ascii=False, indent=4)
                os.system("cls" if os.name == "nt" else "clear")
                print("Arquivo salvo com sucesso.")
               
                while True:
                    # menu
                    print(f"{'-'*20} Menu {'-'*20}")
                    print("1 - Cadastrar novo usuário")
                    print("2 - Listar todos os usuários.")
                    print("3 - Pesquisar usuário através do valor de uma chave")
                    print("4 - Alterar dados de um usuário")
                    print("5 - Deletar usuário de um arquivo")
                    print("6 -Finalizar o Programa")

                    opcao1 = input("Informe a opção desejada: ")

                    match opcao1:
                        case "1":
                            ...
                   

            
            except Exception as e:
                print(f"Não foi possível cadastrar novo arquivo. {e}.")