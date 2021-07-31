from random import randint
print(20* '-=')
print('VAMOS JOGAR PAR OU ÍMPAR')
print(20* '-=')
v = 0
while True:
    valorjogador = int(input('Diga um valor: '))
    computador = randint(0,11)
    total = computador + valorjogador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Você escolher Par ou Ímpar [P/I]')).upper()
        print(f'Você jogou {valorjogador} e o computado jogou {computador}, resultando em um total de {total}')
    if tipo == 'P':
        if total%2 == 0:
            print('Você venceu')
            v += 1
        else:
            print('Você perdeu')
            break
    elif tipo == 'I':
        if total%2 == 1:
            print('Você venceu')
            v+=1
        else:
            print('Você perdeu')
            break
    print('Vamos jogar denovo!')
print('tente novamente!')
print(f'o seu número de vitórias foi de {v}')