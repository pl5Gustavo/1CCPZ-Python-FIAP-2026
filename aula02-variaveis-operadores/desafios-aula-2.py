nome = input('Digite seu nome')

print(f'Boas vindas {nome}')

dia_nascimento = int(input('Digite o dia que você nasceu'))
mes_nascimento = int(input('Digite o mes que você nasceu'))
ano_nascimento = int(input('Digite o ano que você nasceu'))
idade = 2026-ano_nascimento
print(f'Olá {nome}! Você nasceu em {dia_nascimento}/{mes_nascimento}/{ano_nascimento}. Então, você tem {idade} anos')

salario = float(input('Digite quantos reais você ganha'))
imposto = float(input('Digite quantos reais de imposto você paga'))
print(f'Você ganha {salario} reais, e paga {imposto} reais de imposto. Então sobra para você {salario-imposto} reais')