"""
#TODO - atividade: Crie um programa que mostre a hota atual sempre sendo atualizada a cada segundo.
#NOTE - para interromper o programa, use a tecla de atalho ctrl+c
"""
import datetime
import os
import time

while True:
    hora = datetime.datetime.now().strftime("%H:%M:%S")

    os.system("cls")
    print(f"{hora}")
    time.sleep(1)
