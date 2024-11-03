# 37) Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de converção: -1 para binário; -2 para octal -3 para hexadecimal.
num = int(input("Digite um número: "))
convercao = int(input("Digite a base de conversão (1-para binário; 2-para octal; 3-para hexadecimal): "))
if convercao == 1:
    binario = bin(num)
    print(f"Binário: {binario}")
elif convercao == 2:
    octal = oct(num)
    print(f"Octal: {octal}")
elif convercao == 3:
    hexadecimal = hex(num)
    print(f"Hexadecimal: {hexadecimal}")
else:
    print("ERRO! Tente novamente")