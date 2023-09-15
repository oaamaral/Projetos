#Tabela dos numeros
print("Insira três números diferentes")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

#Verificando se são verdadeiros 
if num1 == num2 or num1 == num3 or num2 == num3:
    print("Os números inseridos não são diferentes.")
else:
    if num1 < num2 and num1 < num3:
        print("O menor número é.", num1)
    elif num2 < num3:
        print("O menor número é.", num2)
    else:
        print("O menor número é.", num3)