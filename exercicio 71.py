print('='*30)
print('{:^30}'.format('BANCO DO BRASIL'))
print('='*30)
valor = int(input('Qual valor quer sacar? R$ '))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd>0:
            print(f'Total de {totcéd} células de {céd} R$')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('Volte Sempre ao Banco do Brasil, Tenha um bom dia!!!)