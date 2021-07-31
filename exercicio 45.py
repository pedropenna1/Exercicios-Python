from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0,2)
print('''SUAS OPÇÕES
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
opcao = int(input('Selecione sua jogada'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!!!')
sleep(1)
print('-='*11)
print('O computador escloheu {} '.format(itens[computador]))
print('O jogador jogou {} '.format(itens[opcao]))
print('-='*11)

if computador == 0:
    if opcao == 0:
        print('EMPATE !!!!!!')
    elif opcao == 1:
        print('JOGADOR GANHOU !!!!!')
    elif opcao == 2:
        print('COMPUTADOR GANHOU !!!!!!!')
    else:
        print('JOGADA INVALIDA!!!!')
elif computador == 1:
    if opcao == 0:
        print('COMPUTADOR GANHOU !!!!!!!')
    elif opcao == 1:
        print('EMPATE !!!!!!')
    elif opcao == 2:
        print('JOGADOR GANHOU !!!!!')
    else:
        print('JOGADA INVALIDA!!!!')
elif computador == 2:
    if opcao == 0:
        print('JOGADOR GANHOU !!!!!')
    elif opcao == 1:
        print('COMPUTADOR GANHOU !!!!!!!')
    elif opcao == 2:
        print('EMPATE !!!!!!')
    else:
        print('JOGADA INVALIDA!!!!')
