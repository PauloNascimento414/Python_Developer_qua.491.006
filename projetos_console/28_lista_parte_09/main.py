import os
#lista
nomes = ["Fulano", "Cicrano", "Beltrano", "João", "Maria", "Jóse"]

#exibe a lista
for i in range(len(nomes)):
    print(f"{i}: {nomes[i]}")
print('-'*60)

try:
    if i >= 0 and i < len(nomes):
        i = int(input("Informe o índice que deseja separar: "))
        nome_isolado = nomes.pop(i)
        os.system("cls" if os.name == "nt" else "clear")
        print(f"{nome_isolado} separado com sucesso!")

        # lista exibe os valores sem o item isolado
        for i in range(len(nomes)):
            print(f"{i}: {nomes[i]}")
        print('-'*60)

        #exibe o item isolado
        print(f"Valor isdolado da lista: {nome_isolado}.")
    else:
        print("Índice inválido")
except Exception as e:
    print(f"Não foi possivel executar a operação. {e}.")