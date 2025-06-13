#Declaração de variáveis

x = 5
y = 2
#result = 10 - 50

#operações
soma = x+y
subtracao = x-y
multiplicacao = x*y
divisao = x/y
resto = x%y
potencia = x^y

# saída de dados
#convertendo números para string

#num1 = str(x)
#num2 = str(y)
#result = str(result)
#Operadores aritiméticos
#Concatenação 1° Forma
#print("A soma dos valores:",x, "e", y, "é", x+y, ".")

#Concatenação 2° Forma
#print("A subtatração dos valores de " + x + "e" + y + "é" + x-y + ".")
# Concatenar usando (+) só apenas srting.
#print("A subtatração dos valores de " + x + " e " + y + " é " + result + ".")

#_____________________________________________________________________________________________________________________________________________
#Concatenação 3° Forma
print ("A soma de {} e {} é {}.".format(x, y, soma))

#Concatenação 4° Forma
print(f"A subtração de {x} e {y} é {subtracao}.")
print(f"A multiplicacao de {x} e {y} é {multiplicacao}.")
print(f"A divisao de {x} e {y} é {divisao}.")
print(f"A resto de {x} e {y} é {resto}.")
print(f"{x} elevado a {y} é {potencia}.")

