
cont = 0
num = (int(input('Digite um número de 0 a 10: ')),int(input('Digite mais um número de 0 a 10: ')),int(input('Digite mais um número de 0 a 10: ')),int(input('Digite mais um número de 0 a 10: ')))
for c in num:
    if c%2 == 0:
        cont += 1
print(f'tem-se {num.count(9)} números 9')
print(f'O primeiro número 3 está na posição {num.index(3)+1}')
print(f'O total de números pares digitados são {cont}')

