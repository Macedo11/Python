# 31) Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km e R$0,45 para viagens mais longas.
distancia = int(input("Digite a distância da viagem: "))

if distancia <= 200:
    valor = float(distancia * 0.50)
    print(f"Sua viagem custará: R${valor:.2f}")
else:
    valor = float(distancia * 0.45)
    print(f"Sua viagem custará: R${valor:.2f}")