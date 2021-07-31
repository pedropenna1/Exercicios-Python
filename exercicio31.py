x = (float(input('Qual a distância da viagem em km? ')))
if x > 200:
    y = x*0.45
    print('O custo da viagem terá o valor de R$ {}'.format(y))
else:
    z = x*0.50
    print('O custo da viagem terá o valor de R${}'.format(z))
