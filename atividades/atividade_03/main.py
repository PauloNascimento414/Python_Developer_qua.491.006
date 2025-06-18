"""
#TODO - atividade: Crie um programa que faça as seguintes operações:
- Calcular área de um círculo
- Calcular tamanho de uma circuferência
- sair do programa 
#NOTE - para cada loop, o programa deverá limpar o terminal
"""
#importa biblioteca
import os
import math as m

while True:
        # menu
    print(f"{'-'*20} MENU {'-'*20}")
    print("0 - Calcular área de um círculo")
    print("1 - Calcular tamanho de uma circunferência")
    print("2 - Sair do programa")

    operador = input("Informe a operação desejada: ").strip()

    os.system("cls" if os.name == "nt" else "clear")
    try:
        if operador == "0" or operador == "1":
            raio = float(input("Informe o valor do raio: ").replace(",", "."))
        else:
            pass
        os.system("cls" if os.name == "nt" else "clear")
        match operador:
            case "0":
                area = m.pi * (raio ** 2)
                print(f"A área do círculo com raio {raio} é: {area}")
                continue
            case "1":
                circunferencia = 2 * m.pi * raio
                print(f"A circunferência do círculo com raio {raio} é: {circunferencia}")
                continue       
            case "2":
                print("Saindo do programa...")
                break
            case _:
                print("Operação inválida. Tente novamente.")
                
    except Exception as e:
        print(f"Não foi possível calcular. {e}.")
