# declaração de variáveis
aluno = input("Informe o nome do aluno: ")
media = float(input("Informe média do aluno: ").replace(",", "."))

# estrutura de decisão
if media >= 0 and media <= 10:
    if media >= 7:
        print(f"{aluno} está aprovado.")
    elif media >= 5:
        print(f"{aluno} está recuperação.")
    else:
        print(f"{aluno} está reprovado.")
else:
    print("Nota inválida.")

