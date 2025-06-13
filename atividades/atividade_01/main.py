""""
# TODO - atividade:
Crie um programa que receba do usuário o valor do etanol e da gasolina em 
reais, e informe para o usuário qual o melhor combustível para abastecer.
# NOTE -  o usuário poderá informar várias vezes os valores , e irá encerrar o programa quando desejar.
# NOTE - cálculo: compensa etanol caso ele tenha 70% do valor da gasolina.
"""
# Loop infinito
while True:
    # menu
    print(f"{'-'*20} MENU {'-'*20}")
    print("0 - Encerrar o programa")
    print("1 - Calculo Combustiveis")

    operador = input("Informe a operação desejada: ").strip()
    
    match operador:
        case "0":
            print("Programa encerrado.")
            break
        case "1":
            try:
                gasolina = float(input("Informe o valor de Gasolina: ").replace(",", "."))
                alcool = float(input("Informe o valor de Álcool: ").replace(",", "."))
                percentual = (alcool / gasolina) * 100
                if percentual <= 70:
                    print(f"{percentual}% - Abasteça Álcool.")
                else: 
                    print(f"{percentual}% - Abasteça Gasolina.")

            except Exception as e:
                print(f"Não foi possivel calcular. {e}.")
            finally:
                continue
        case _:
            print("Operador inválido")
            continue 
