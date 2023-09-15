# INFORME SUA DATA DE NASCIMENTO
ano_atual = 2023
nascimento = int(input("Qual sua data de nascimento? "))
idade = ano_atual - nascimento
resp = input("Você ja fez aniversario esse ano? ")

if resp == "Não":
    idade -= 1

print("Sua idade é", idade)