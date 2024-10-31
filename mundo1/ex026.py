# 26) Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição ela aparece a primeira vez.
# Em que posição ela aparece a última vez.

frase = str(input("Digite uma frase: ")).upper()
frase = frase.strip()
quantidade = frase.count('A')
primeira = frase.index('A')
ultima = frase.rfind('A')

print(f"A letra 'a' aparece {quantidade} vezes")
print(f"A letra 'a' aparece pela primeira vez no índice: {primeira}")
print(f"A letra 'a' aparece pela útima vez no índice: {ultima}")
