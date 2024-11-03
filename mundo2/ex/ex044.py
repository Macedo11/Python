# 44) Elabore um programa que pegue o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamanto: -à vista dinheiro/cheque: 10% de desconto; -à vista no cartão: 5% de desconto; -em até 2x no cartão: preço normal; -3x ou mais no cartão: 20% de juros.
produto = float(input("Digite o valor do produto: "))
forma_pagamento = str(input("Digite a forma de pagamento: dinheiro, cheque, cartão a vista, 2x ou 3x: "))

if forma_pagamento == "dinheiro" or forma_pagamento == "cheque":
    desconto = produto - (produto * 0.1)
    print(f"Você ganhou 10% de desconto: R${desconto:.2f}")
elif forma_pagamento == "cartão a vista":
    desconto = produto - (produto * 0.05)
    print(f"Você ganhou 5% de desconto: R${desconto:.2f}")
elif forma_pagamento == "2x":
    print(f"2x não tem desconto: R${produto:.2f}")
elif forma_pagamento == "3x":
    juros = produto + (produto * 0.3)
    print(f"3x recebe juros de 30%: {juros:.2f}")
else:
    print("ERRO! Tente novamente.")