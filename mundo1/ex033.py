# 33) Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite o último número: "))

lista = [num1, num2, num3]
menor = min(lista)
maior = max(lista)

print(f"O menor número digitado é: {menor}")
print(f"O maior número digitado é: {maior}")