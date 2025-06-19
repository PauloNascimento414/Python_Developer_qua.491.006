"""
#TODO - atividade: Crie um programa que recebe do usuário o nome e a idade, e
em seguida, mostre um menu de filmes com suas respectivas classificações indicativas
e salas de exibição. Exemplo:
- Sala 1: A Roda Quadrada - Livre
- Sala 2: A Volta dos Que Não Foram - 12 anos
- Sala 3: Poeira em Alto Mar - 14 anos
- Sala 4: As Tranças do Rei Careca - 16 anos
- Sala 5: A Vingança do Peixe Frito - 18 anos
O usuário deve escolher a sala que está passando o filme que deseja assistir.
- Se o usuário tiver a idade mínima ou mais para ver o filme, o programa
imprimi o ingresso com o nome do usuário, a sala, o nome do filme, a data e a hora de compra do ingresso,
e deseje bom filme, e em seguida encerra o programa.
- Se o usuário não tiver a idade mínima para ver o filme, o programa bloqueia a sua entrada, e re-exibe
o menu de filmes para que ele escolha outro filme.
"""
import os
import datetime
from datetime import date

nome = input("Informe o seu nome: ").strip()
idade = int(input("Informe a sua idade: "))
os.system("cls" if os.name == "nt" else "clear")

while True:
        # menu
    print(f"{'-'*20} FILMES {'-'*20}")
    print("Sala 1: A Roda Quadrada - Livre")
    print("Sala 2: A Volta dos Que Não Foram - 12 anos")
    print("Sala 3: Poeira em Alto Mar - 14 anos")
    print("Sala 4: As Tranças do Rei Careca - 16 anos")
    print("Sala 5: A Vingança do Peixe Frito - 18 anos")

    filme = input("Informe a sala do filme: ").strip()
    os.system("cls" if os.name == "nt" else "clear")
    try:
        match filme:
            case "1":
                print("A Roda Quadrada")
                print(f"{nome}")
                print("Sala 1")
                hoje = date.today().strftime("%d/%m/%Y")
                print(f"Data da compra: {hoje}.")
                hora = datetime.datetime.now().strftime("%H:%M:%S")
                print(f"Hora da compra: {hora}.")
                break
            case "2":
                if idade >= 12:
                    print("A Volta dos Que Não Foram")
                    print(f"{nome}")
                    print("Sala 2")
                    hoje = date.today().strftime("%d/%m/%Y")
                    print(f"Data da compra: {hoje}.")
                    hora = datetime.datetime.now().strftime("%H:%M:%S")
                    print(f"Hora da compra: {hora}.")
                    break
                else:
                    print(f"{nome} não tem a idade mínima para assistir o filme.")
                continue
            case "3":
                if idade >= 14:
                    print("Poeira em Alto Mar")
                    print(f"{nome}")
                    print("Sala 3")
                    hoje = date.today().strftime("%d/%m/%Y")
                    print(f"Data da compra: {hoje}.")
                    hora = datetime.datetime.now().strftime("%H:%M:%S")
                    print(f"Hora da compra: {hora}.")
                    break
                else:
                    print(f"{nome} não tem a idade mínima para assistir o filme.")
                continue
            case "4":
                if idade >= 16:
                    print("As Tranças do Rei Careca")
                    print(f"{nome}")
                    print("Sala 4")
                    hoje = date.today().strftime("%d/%m/%Y")
                    print(f"Data da compra: {hoje}.")
                    hora = datetime.datetime.now().strftime("%H:%M:%S")
                    print(f"Hora da compra: {hora}.")
                    break
                else:
                    print(f"{nome} não tem a idade mínima para assistir o filme.")
                continue
            case "5":
                if idade >= 18:
                    print("A Vingança do Peixe Frito")
                    print(f"{nome}")
                    print("Sala 5")
                    hoje = date.today().strftime("%d/%m/%Y")
                    print(f"Data da compra: {hoje}.")
                    hora = datetime.datetime.now().strftime("%H:%M:%S")
                    print(f"Hora da compra: {hora}.")
                    break
                else:
                    print(f"{nome} não tem a idade mínima para assistir o filme.")
                continue      
            case _:
                print("Operação inválida. Tente novamente.")
                continue
    except Exception as e:
        print(f"Não foi possivel selecionar a sala.{e}.")


