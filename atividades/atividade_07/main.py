"""
#TODO - atividade: Crie um programa que faça as seguintes operações:
- Cadastre novo nome na lista
- Liste todos os nomes na lista
- Pesquise por um nome na lista
- Altere um nome na lista
- Exclua um nome na lista
#NOTE - a lista deve começar vazia: lista = []
"""

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

    opcao = input("Informe a opção desejada: ").strip()
    try:
        match opcao:
            case "1":
                # usuário informa nome a ser acrescetada na lista
                novo_nome = input("Informe o novo nome: ").title().strip()
                # novo nome é inserido na lista
                nomes.append(novo_nome)
            case "2":
                for nome in nomes:
                    print(nome)
            case "3":
                nome_pesquisada = input("Informe o nome a ser pesquisado: ").title().strip()
                # programa conta quantas vezes ocorre o item pesquisado
                qtde = nomes.count(nome_pesquisada)
                # programa indica quantas vezes o item foi encontrado
                print(f"{nome_pesquisada} foi encontrado {qtde} vezes na lista.")
            case "4":
                # exibe a lista de compras
                for i in range(len(nomes)):
                    print(f"Índice {i}: {nomes[i]}.")
                    # usuário informa o índice a ser alterado
                    i = int(input("Inorme a posição do índice a ser alterado: "))
                    if i >= 0 and i <= len(nomes):
                        nomes[i] = input("Infome o novo valor: ").capitalize().strip()
                        print("Item alterado com sucesso!")
                    else:
                        print("Índice inválido")
            case "5":
                for i in range(len(nomes)):
                    print(f"{i}: {nomes[i]}.")
                i = int(input("Informe a posição do nome na lista: "))
                if i >= 0 and i<= len(nomes):
                    del(nomes[i])
                    print("Nome excluído com sucesso!")
                else:
                    print("Posição inválida.")
            case _:
                print("Opção inválido.")
    except Exception as e:
            print(f"Não foi possível selecionar a opção desejada.{e}.")

