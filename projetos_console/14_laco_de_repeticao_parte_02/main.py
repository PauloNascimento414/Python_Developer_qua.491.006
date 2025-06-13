# Loop infinito
while True:
    # menu
    print(f"{'-'*20} MENU {'-'*20}")
    print("0 - Encerrar o programa")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")

    operador = input("Informe a operação desejada: ").strip()
    
    match operador:
        case "0":
            print("Programa encerrado.")
            break
        case "1":
            try:
                x = float(input("Informe o valor de X: ").replace(",", "."))
                y = float(input("Informe o valor de Y: ").replace(",", "."))

                print(f"{x} + {y} = {x+y}")
            except Exception as e:
                print(f"Não foi possivel somar. {e}.")
            finally:
                continue        
        case "2":
            try:
                x = float(input("Informe o valor de X: ").replace(",", "."))
                y = float(input("Informe o valor de Y: ").replace(",", "."))

                print(f"{x} - {y} = {x-y}")
            except Exception as e:
                print(f"Não foi possivel subtrair. {e}.")
            finally:
                continue 
        case "3":
            try:
                x = float(input("Informe o valor de X: ").replace(",", "."))
                y = float(input("Informe o valor de Y: ").replace(",", "."))

                print(f"{x} x {y} = {x*y}")
            except Exception as e:
                print(f"Não foi possivel multiplicar. {e}.")
            finally:
                continue 
        case "4":
            try:
                x = float(input("Informe o valor de X: ").replace(",", "."))
                y = float(input("Informe o valor de Y: ").replace(",", "."))

                print(f"{x} / {y} = {x/y}")
            except Exception as e:
                print(f"Não foi possivel Dividir. {e}.")
            finally:
                continue 
        case _:
            print("Operador inválido")
            continue 