# 40) Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida: -Média abaixo de 5.0: REPROVADO; -Média entre 5.0 e 6.9: RECUPERAÇÃO; -Média 7.0 ou superior: APROVADO.
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3

if media < 5.0:
    
    print(f"Média {media:.2f}\n REPROVADO")
elif media >= 5.0 and media <= 6.9:
    print(f"Média {media:.2f}\n RECUPERAÇÃO")
elif media > 6.9:
    print(f"Média {media:.2f}\n Parabéns! APROVADO")
else:
    print("ERRO! Tente novamente")