"""
#TODO - atividade: Crie um programa que faça as seguintes funções:
- Cadastre um novo usuário
- Liste todos os usuários cadastrados
- Altere os dados de um usuário
- Fazer sorteio de usuário
- Exclua um usuário
- Saida do programa
#NOTE - Dados do usuário:
- Nome completo
- Data de nascimento
- E-mail
- CPF
- Telefone
- Gênero
- Data do cadastro
- Hora do cadastro
"""
import os
import datetime
from datetime import date
import random
#lista
usuarios = []

while True:
    #dicionario
    usuario = {}
    # menu
    print(f"{'-'*20} Menu {'-'*20}")
    print("1 - Cadastre um novo usuário")
    print("2 - Liste todos os usuários cadastrados")
    print("3 - Altere os dados de um usuário")
    print("4 - Fazer sorteio de usuário")
    print("5 - Exclua um usuário")
    print("6 - Sair do programa")

    opcao = input("Informe a opção desejada: ").strip()
    os.system("cls" if os.name == "nt" else "clear")
    match opcao:
        case "1":
            try:
                hoje = date.today().strftime("%d/%m/%Y")
                hora = datetime.datetime.now().strftime("%H:%M:%S")
                usuario['nome'] = input("Informe o nome do usuário: ").strip().title()
                usuario['nascimento'] = input("Informe a data de nascimento do usuário: ").strip()
                usuario['email'] = input("Informe o e-mail do usuário: ").strip().lower()
                usuario['cpf'] = input("Informe o CPF do usuário: ").strip()
                usuario['telefone'] = input("Informe o telefone do usuário: ").strip()
                usuario['genero'] = input("Informe o gênero do usuário: ").strip()
                usuario['data'] = hoje
                usuario['hora'] = hora
                usuarios.append(usuario)
                os.system("cls" if os.name == "nt" else "clear")
                print(f"Usuário {usuario.get('nome')} cadastrado com sucesso.")
            except Exception as e:
                 print(f"Não foi possível inserir os dados do usuário. {e}.")
            finally:
                 continue
        case "2":
            try:
                for i in range(len(usuarios)):
                    print(f"Índice: {i}")
                    for chave in usuarios[i]:
                        print(f"{chave.capitalize()}: {usuarios[i].get(chave)}")
                    print("-"*40)
            except Exception as e:
                 print(f"Não foi possível listar os usuário. {e}.")
            finally:
                 continue
        case "3":
            try:
                i = int(input("Informe o índice que deseja alterar: "))
                if i>= 0 and i < len(usuarios):
                    print(f"{'-'*20} Dados do usuário{'-'*20}")
                    for chave in usuarios[i]:
                        print(f"{chave.capitalize()}: {usuarios[i].get(chave)}")
                    print("\n")
                    while True:
                        # usuário informa a chave que deseja alterar
                        chave_escolhida = input("Informe a chave que deseja alterar: ").lower().strip()
                        if chave_escolhida in usuarios[i]:
                            usuarios[i][chave_escolhida] = input(f"Informe o novo valor de {chave_escolhida}: ")
                            print("Chave alterada com sucesso.")
                        else:
                            print("Chave inexistente.")
                        while True:
                            prosseguir = input("Deseja alterar outra chave? (s/n): ").strip().lower()
                            if prosseguir ==  's' or prosseguir == 'n':
                                break
                            else:
                                continue
                        match prosseguir:
                            case "s":
                                continue
                            case "n":
                                break
                else:
                    print("Índice inválido.")                        
            except Exception as e:
                print(f"Não foi possível inserir alterar dados do usuário. {e}.")
            finally:
                 continue        
        case "4":
                try:
                    i = random.randint(0, len(usuarios) -1)
                    print("Usuário sorteado:")
                    for chave in usuarios[i]:
                        print(f"{chave.capitalize()}: {usuarios[i].get(chave)}")
                except Exception as e:
                    print(f"Não foi possível sortear usuário")
        case "5":
            try:
                i = int(input("Informe o índice a ser excluído: "))
                if i >= 0 and i < len(usuarios):
                    for chave in usuarios[i]:
                        print(f"{chave.capitalize()}: {usuarios[i].get(chave)}")
                    while True:
                        excluir = input("Tem certeza? (s/n): ").strip().lower()
                        if excluir == 's' or excluir == 'n':
                            break
                        else:
                            print("Opção inválida.")
                            continue
                    match excluir:
                        case "s":
                            del usuarios[i]
                            os.system("cls" if os.name == "nt" else "clear")
                            print("Usuário excluído com sucesso.")
                        case "n":
                            os.system("cls" if os.name == "nt" else "clear")
                            print("Usuário não excluído.")
                else:
                    print("Índice invalido.")  
            except Exception as e:
                print(f"Não foi possível excluir o usuário.")
        case "6":
            os.system("cls" if os.name == "nt" else "clear")
            print("Programa Finalizado.")
            break
        case _:
            try:
                os.system("cls" if os.name == "nt" else "clear")
                print("Opção inválido.")
                continue
            except Exception as e:
                print(f"Não foi possível selecionar a opção desejada.{e}.")
