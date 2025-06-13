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
                if percentual < 70:
                    print(f"{percentual:.2f}% - Abasteça Álcool.")
                else: 
                    print(f"{percentual:.2f}% - Abasteça Gasolina.")

            except Exception as e:
                print(f"Não foi possivel calcular. {e}.")
            finally:
                continue
        case _:
            print("Operador inválido")
            continue 
"""
#TODO - Código feito pelo professor 

While True:
    try:
        etanol = float(input("Informe o valor do etanol: R$ ").replace(",", "."))
        gasolina = float(input("Informe o valor do gasolina: R$ ").replace(",", "."))
        calculo = (etanol/gasolina)*100
        result = "gasolina" if etanol > gasolina*0.7 else "etanol"

        print(f"Resultado = {calculo:.2f}%. Compensa abastecer com {result}.")

        opcao = input("Deseja refazer o cáculo? (s/n)").lower().strip()
        match opcao:
            case "s":
                continue
            case "n":
                break
             case _:
                print("opção inválida.")
                continue
    except Exception as e:
        print(f"Não foi possível executar operação. {e}.")
        continue            
"""