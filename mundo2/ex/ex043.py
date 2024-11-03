# 43) Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# -Abaixo de 18,5: Abaixo do Peso; Entre 18,5 e 25: Peso ideal; -25 até 30: Sobrepeso; -30 até 40: Obesidade; -Acima de 40: Obesidade mórbida.
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a alura: "))
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"Abaixo do Peso: {imc:.2f}")
elif imc >= 18.5 and imc <= 25:
    print(f"Você está no peso ideal: {imc:.2f}")
elif imc > 25 and imc <= 30:
    print(f"Sobrepeso: {imc:.2f}")
elif imc > 30 and imc <= 40:
    print(f"Obesidade: {imc:.2f}")
else: 
    print(f"Obesidade Mórbida: {imc:.2f}")