nome = str(input("Digite seu nome completo: "))

maius = nome.upper()
minus = nome.lower()
nomeCompLetras = len(list(filter(str.isalpha, nome)))
achandoNome = nome.split()
primeiroNome = achandoNome[0]


print('Analisando seu nome...')
print(f'Seu nome em letras maiúsculas fica: {maius}')
print(f'Seu nome em letras minúsculas fica: {minus}')
print(f'Seu nome completo tem {nomeCompLetras}')

print(primeiroNome)