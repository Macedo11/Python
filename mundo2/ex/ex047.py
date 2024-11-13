# 47) Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

for i in range (0, 51, 2):
    if i % 2 == 0:
        print(i, end=" ")
    else:
        print("Não existe números pares")