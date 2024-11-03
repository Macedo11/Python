# 45) Crie um programa que faça o computador jogar Jokenpô com você.
import random

escolha = int(input("Escolha entre 1-papel, 2-pedra, 3-tesoura: "))
escolha_bot = random.randint(1, 3)

if escolha_bot == 1 and escolha == 3:
    print("Parabéns! Você venceu!")
elif escolha_bot == 2 and escolha == 1:
    print("Parabéns! Você venceu!")
elif escolha_bot == 3 and  escolha == 2:
    print("Parabéns! Você venceu!")
else:
    print("Você perdeu")
