# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".
cidade = str(input("Digite o nome da cidade: "))
frase = cidade.split()
cidade_natal = frase[0]
cidade_natal = cidade_natal.upper()

if cidade_natal == "SANTO":
    print(f"Você nasceu na cidade Santo!")
else:
    print(f"Você não nasceu nessa cidade! \nTente Novamente")