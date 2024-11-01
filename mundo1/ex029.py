# 29) Escreva um programa que leia a velocidade do carro. Se ele ultrapassar 80km/h. Mostre uma mensagem dizendo que 
# ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velo = int(input("Digite a velocidade do carro: "))

if velo >= 80:
    multa = float((velo - 80) * 7)
    print(f"Você ultrapassou o limite de velocidade de 80Km/h!")
    print(f"Multado no valor de R${multa:.2f}")