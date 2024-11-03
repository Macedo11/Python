# 42) Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar o tipo de triângulo será formado:
# -Equilátero: todos os lados iguais; -Isósceles: dois lados iguais; -Escaleno: todos os lados diferentes.
lado1 = int(input("Digite o comprimento do primeiro lado: "))
lado2 = int(input("Digite o comprimento do segundo lado: "))
lado3 = int(input("Digite o comprimento do terceiro lado: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print("Os lados formam um triângulo!")

    if lado1 == lado2 == lado3:
        print("EQUILÁTERO: Todos os lados são iguais")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("ISÓSCELES: Dois lados são iguais")
    else:
        print("ESCALENO: Todos os lados são diferentes")
else:
    print("Os lados NÃO formam um triângulo")