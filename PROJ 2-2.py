# Solicita as notas do usuário
nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota:  "))
nota3 = float(input("Insira a terceira nota: "))
nota4 = float(input("Insira a quarta nota:   "))

# Calcula a média das notas
media = (nota1 + nota2 + nota3 + nota4) / 4

# Verifica se o estudante foi aprovado
if media >= 7:
    print("Aluno aprovado.")

else:
    print("O aluno não passou de periodo.")

# Exibe a média
print(f"Sua média é: {media:.2f}")