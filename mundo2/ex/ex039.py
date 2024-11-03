# 39) Faça um programa que leia o ano de um nascimento de um jovem e informe, de acordo com sua idade:
# -Se ele ainda vai se alistar ao serviço militar; - Se é a hora se alistar; -Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou o prazo.
idade = int(input("Digite a sua idade: "))

if idade < 18:
    diferenca = 18 - idade
    print(f"Falta {diferenca} ano(s) para se alista")
elif idade == 18:
    print("Você está na idade de se alistar")
else:
    diferenca = idade - 18
    print(f"Você passou do prazo! Se passaram {diferenca} ano(s)")