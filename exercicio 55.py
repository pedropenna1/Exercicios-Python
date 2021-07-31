maior = 0
menor = 0
for n in range (1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(n)))
    if n == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso lido é de {}'.format(maior))
print('O menor peso lido é de {}'.format(menor))