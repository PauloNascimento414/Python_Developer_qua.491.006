"""
#TODO - atividade: Crie um programa em que o usuário informa um ano e o programa exibe todo o calnedário do ano informado pelo usuário
#NOTE - O Usuário poderá informar qualquer ano a partir de 1900.
#NOTE - use a biblioteca 'calendar'
"""

import calendar
try:
    ano = int(input("Digite o ano: "))
    if ano >= 1900:
        calendario = calendar.calendar(ano)
        print(f"{calendario}")
    else:
        print("Digite um ano a partir de 1900.")
except Exception as e:
    print(f"Não foi possivel mostrar o calendario.{e}.")