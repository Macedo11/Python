# 34) Escreva um programa que pergunte o salário e calcule o valor do seu aumento. Para salários superiores a R$1.250,00, calcule um aumento de %10. Para os inferiores ou iguais o aumento é de 15%.
salario = float(input("Digite o valor do seu salário: "))

if salario > 1250:
    novo_salario = salario + (salario * 0.1)
    print(f"Você ganhou um aumento de 10%: R${novo_salario:.2f}")
else:
    novo_salario = salario + (salario * 0.15)
    print(f"Você ganhou um aumento de 15%: R${novo_salario:.2f}")