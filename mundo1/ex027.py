# 27) Faça um programa que leia o nome completo de uma pessoa. Mostrando em seguida o primeiro e o útlimo nome separadamente.
#Ex: Ana maria de Souza
#primeiro = Ana
#último = Souza
nome_completo = str(input("Digite seu nome completo: ")).strip()
nome_separado = nome_completo.split()
primeiro_nome = nome_separado[0]
ultimo_nome = nome_separado[-1]

print(f"O primeiro nome é: {primeiro_nome}")
print(f"O último nome é: {ultimo_nome}")