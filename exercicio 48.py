soma = 0
cont = 0
for c in range (1, 501, 2):
    if c%3 == 0:
        print(c)
        soma = soma + c
        cont = cont + 1
print('A soma de todos os valores são:{}'.format(soma))
print('Teve um total de {} números'.format(cont))