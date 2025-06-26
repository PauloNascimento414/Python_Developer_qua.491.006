"""
#TODO - atividade: Crie um programa que receba de um professor várias notas de um aluno de 0 a 10
(não importa quantas notas). Ao final do programa, a média das notas deverá ser calculada e informada, e
em seguida, o programa irá informar se o aluno:
- Foi aprovado, caso média for maior ou igual a 7
- Ficou de recuperação, caso média for entre 5 e 7
- Foi reprovado, caso média for menor que 5.
"""
import os
notas = []

while True:
    # menu
    print(f"{'-'*20} Menu {'-'*20}")
    print("1 - Cadastre as notas do aluno")
    print("2 - Média das notas do aluno")
    print("3 - Sair do programa")

    opcao = input("Informe a opção desejada: ").strip()
    os.system("cls" if os.name == "nt" else "clear")
    match opcao:
        case "1":
            try:
                # usuário informa a nota a ser acrescetada na lista
                nova_nota = float(input("Informe nota do aluno: "))
                if nova_nota >= 0 and nova_nota <= 10:
                    # novo nota é inserido na lista
                    notas.append(nova_nota)
                    print(f"{nova_nota} inserida com sucesso!")
                else:
                    print("Nota inválida.")
            except Exception as e:
                 print(f"Não foi possível inserir a nota do aluno. {e}.")
            finally:
                 continue
        case "2":
            try:
                somar_notas = sum(notas)
                media = somar_notas / len(notas)
                if media >= 7:
                    print(f"Média: {media:.2}. Aluno aprovado!")
                elif media >= 5:
                    print(f"Média: {media:.2}. Aluno em recuperação!")
                else:
                    print(f"Média: {media:.2}. Aluno reprovado!")
            except Exception as e:
                print(f"Não foi possível calcular a média.")
            finally:
                continue
        case "3":
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