# 36) Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da pretação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
valor_casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o valor do salário: "))
anos = int(input("Digite quantidade de anos à pagar: "))

meses = int(anos * 12)
prestacao = valor_casa / meses

if prestacao > (salario * 0.3):
    print("Você não pode pagar a prestação da casa!")
else: 
    print(f"Sua prestação ficará no valor de R${prestacao:.2f}, {anos} anos para pagar")