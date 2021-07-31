listagem = ('lapis',1.75,
            'Borracha', 2.75,
            'caderno', 6,
             'lapiseira',5)
print('-' *30)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('-' *30)
for pos in range (0,len(listagem)):
    if pos%2 == 0:
        print(f'{listagem[pos]:.<30}',end=' ')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' *30)