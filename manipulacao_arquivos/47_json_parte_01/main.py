# importações

import json

try:
    #input
    arquivo = input("Informe o nome do arquivo (sem extensão): ").strip().lower()

    # lê o json e desserializa em um dicionário
    with open(f"{arquivo}.json", "r", encoding="utf-8") as f:
        dados = json.load(f)
    # output
    print(f"{'-'*20} Dados {'-'*20}\n")
    for dado in dados:
        for chave in dado:
            print(f"{chave.capitalize()}: {dado.get(chave)}")
        print("-"*47)
except Exception as e:
    print(f"Não foi possível ler arquivo JSON.{e}.")