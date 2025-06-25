"""
#TODO - atividade: Crie um programa que faça as seguintes operações:
- Cadastre novo nome na lista
- Liste todos os nomes na lista
- Pesquise por um nome na lista
- Altere um nome na lista
- Exclua um nome na lista
#NOTE - a lista deve começar vazia: lista = []
"""
import os
# lista
nomes = []

while True:
    # menu
    print(f"{'-'*20} Menu {'-'*20}")
    print("1 - Cadastre novo nome na lista")
    print("2 - Liste todos os nomes na lista")
    print("3 - Pesquise por um nome na lista")
    print("4 - Altere um nome na lista")
    print("5 - Exclua um nome na lista")
    print("6 - Sair do programa")

    opcao = input("Informe a opção desejada: ").strip()
    os.system("cls" if os.name == "nt" else "clear")
    match opcao:
        case "1":
            try:
                # usuário informa nome a ser acrescetada na lista
                novo_nome = input("Informe o novo nome: ").title().strip()
                # novo nome é inserido na lista
                nomes.append(novo_nome)
                print(f"{novo_nome} inserido com sucesso!")
            except Exception as e:
                 print(f"Não foi possível inserir novo nome. {e}.")
            finally:
                 continue
        case "2":
            try:    
                for i in range(len(nomes)):
                    print(f"{i}: {nomes[i]}")
                print('-'*40)
            except Exception as e:
                print(f"Não foi possível exibir a lista.{e}.")
            finally:        
                continue
        case "3":
                nome_pesquisada = input("Informe o nome a ser pesquisado: ").title().strip()
                # programa conta quantas vezes ocorre o item pesquisado
                os.system("cls" if os.name == "nt" else "clear")
                qtde = nomes.count(nome_pesquisada)
                # programa indica quantas vezes o item foi encontrado
                print(f"{nome_pesquisada} foi encontrado {qtde} vezes na lista.")
                continue
        case "4":
            try:
                # exibe a lista de nomes
                for i in range(len(nomes)):
                    print(f"Índice {i}: {nomes[i]}.")
                    # usuário informa o índice a ser alterado
                i = int(input("Informe a posição do índice a ser alterado: "))
                if i >= 0 and i < len(nomes):
                    nomes[i] = input("Infome o novo nome: ").title().strip()
                    os.system("cls" if os.name == "nt" else "clear")
                    print("Nome alterado com sucesso!")
                else:
                    print("Índice inválido")
            except Exception as e:
                        print(f"Não foi possível alterar. {e}.")
            finally:
                 continue
        case "5":
            try:   
                for i in range(len(nomes)):
                    print(f"{i}: {nomes[i]}.")
                i = int(input("Informe a posição do nome na lista: "))
                if i >= 0 and i < len(nomes):
                    os.system("cls" if os.name == "nt" else "clear")
                    del(nomes[i])
                    print("Nome excluído com sucesso!")
                else:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("Índice inválida.")
            except Exception as e:
                        print(f"Não foi possível deletar. {e}.")        
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

