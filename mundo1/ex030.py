# 30) Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar.
num = int(input("Digite um número: "))
if num % 2 == 0:
    print(f"{num} é um número par!")
else:
    print(f"{num} é um número ímpar!")