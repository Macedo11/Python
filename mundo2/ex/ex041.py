# 41) A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de aum atleta e mostre sua categoria, de acordo com a idade:
# -Até 9 anos: MIRIM; -Até 14 anos: INFANTIL; -Até 19 anos: JUNIOR; -Até 20 anos: SÊNIOR; -Acima: MASTER.
idade = int(input("Digite sua idade: "))

if idade <= 9:
    print("MIRIM")
elif idade <= 14:
    print("INFANTIL")
elif idade <= 19:
    print("JUNIOR")
elif idade <= 20:
    print("SÊNIOR")
else:
    print("MASTER")