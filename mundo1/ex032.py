# 32) Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
ano = int(input("Digite um ano: "))

if ano % 4 == 00:
    print(f"{ano} É um ano Bissexto!")
else: print(f"{ano} NÃO é uma ano Bissexto!")