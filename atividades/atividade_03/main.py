"""
#TODO - atividade: Crie um programa que faça as seguintes operações:
- Calcular área de um círculo
- Calcular tamanho de uma circuferência
- sair do programa 
#NOTE - para cada loop, o programa deverá limpar o terminal
"""
#importa biblioteca
import os as o
import math as m

while True:
        # menu
    print(f"{'-'*20} MENU {'-'*20}")
    print("0 - Calcular área de um círculo")
    print("1 - Calcular tamanho de uma circunferência")
    print("2 - Sair do programa")

    operador = input("Informe a operação desejada: ").strip()
   
    
    

    match operador:
        case "0":
            try:
                raio = float(input("Informe o valor do raio: ").replace(",", "."))    
                area = m.pi * (raio ** 2)
                print(f"A área do círculo com raio {raio} é: {area}")
            except Exception as e:
                print(f"Não foi possível calcular a área. {e}.")
                break
        case "1":
            try:
                raio = float(input("Informe o valor do raio: ").replace(",", "."))
                circunferencia = 2 * m.pi * raio
                print(f"A circunferência do círculo com raio {raio} é: {circunferencia}")
            except Exception as e:
                print(f"Não foi possível calcular a circunferência. {e}.")
                continue
        case "2":
            print("Saindo do programa...")
            break
        case _:
            print("Operação inválida. Tente novamente.")
            continue
    o.system("cls")
