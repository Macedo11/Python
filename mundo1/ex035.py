# 35) Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
reta1 = int(input("Digite o comprimento da primeira reta: "))
reta2 = int(input("Digite o comprimento da segunda reta: "))
reta3 = int(input("Digite o comprimento da terceira reta: "))

if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print("As retas formam um triângulo!")
else:
    print("As retas NÃO forma um triângulo.")