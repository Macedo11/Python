# 28) Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
num_secreto = random.randint(0, 5)
chute = int(input("Tente advinhar um número de 0 a 5 que eu pensei: "))

if chute == num_secreto:
    print(f"Parabens! Você acertou o numero que eu pensei: {num_secreto}")
else:
    print("Infelizmente você errou!")