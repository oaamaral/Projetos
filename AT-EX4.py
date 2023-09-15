# INFORMAR SALARIO
salario = float(input("Informe seu salario:"))
abono= 0

if salario < 5000:
    abono = salario * 0.15

else:
    abono = salario * 0.1
print (f"Seu abono é de fim de ano: R$ {abono:.2f}")