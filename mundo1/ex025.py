# 25) Crue um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
nome_completo = str(input("Você tem Silva no nome?: ")).strip()

if "SILVA" in nome_completo.upper():
    print(True)
else:
    print(False)
