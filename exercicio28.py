from random import randint
print('Vou pensar em um número entre 0 e 5, tente adivinhar')
x = randint(0,5)
y = int((input('Digite um número de 0 a 5: ')))
if y == x:
    print('Parabéns você acertou!')
else:
    print('Você errou, tente novamente.')
