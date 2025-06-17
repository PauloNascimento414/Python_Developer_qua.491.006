"""
#TODO - atividade: Crie um programa que receba do usuário, o nome, o peso em Kg, 
# e a altura em metros, e calcule o valor do IMC (Ìndice de Massa Corporal).
O Programa deve mostrar o valor do IMC arredondado para 2 casas decimais, e mostrar o
diagnóstico do usuário com base nos seguintes valores:
- Caso o IMC seja menor que 18.5 = abaixo do peso.
- Caso o IMC seja maior ou igual a 18.5 e menor que 25 = peso ideal.
- Caso o IMC seja maior ou igual a 25 e menor que 30 = acima do peso.
- Caso o IMC seja maior ou igual a 30 e menor que 35 = obeso.
- Caso o IMC seja maior ou igual a 35 e menor que 40 = Obesidade nível 2.
- Caso o IMC seja maior ou igual a 40 = Obesidade mórbida.
#NOTE -  o usuário deverá informar o encerramento do programa, ou seja, ele poderá repetir o cálculo  quantas vezes quiser.

"""

while True:
    try:
        #entrada de dados
        nome = input("Informe o nome do usuário: ").title().strip()
        peso = float(input("Informe o peso do usuário em Kg: ").replace(",", "."))
        altura = float(input("Informe o altura do usuário em metros: ").replace(",", "."))
        imc = peso/(altura**2)

        if imc < 18.5:
            print(f"IMC = {imc:.2f}. {nome} está abaixo do peso.")
        elif imc >= 18.5 and imc < 25.0:
            print(f"IMC = {imc:.2f}. {nome} está com peso ideal.")
        elif imc >= 25.0 and imc < 30.0:
            print(f"IMC = {imc:.2f}. {nome} está acima do peso.")
        elif imc >= 30.0 and imc < 35.0:
            print(f"IMC = {imc:.2f}. {nome} está obeso.")
        elif imc >= 35.0 and imc < 40.0:
            print(f"IMC = {imc:.2f}. {nome} está com obesidade nível 2.")
        else:
            print(f"IMC = {imc:.2f}. {nome} está com obesidade mórbida.")

        while True:
            opcao = input("Deseja refazer o cáculo? (s/n): ").strip().lower()
            if opcao == "s" or opcao == "n":
                break
            else:
                print("opção inválida.")
                continue
            
        match opcao:
            case "s":
                continue
            case "n":
                break

    except Exception as e:
        print(f"Não foi possível executar operação. {e}.")
        continue