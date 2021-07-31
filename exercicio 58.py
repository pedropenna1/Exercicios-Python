from random import randint
print('Vou pensar em um número entre 0 e 5, tente adivinhar')
x = randint(0,5)
y = int((input('Digite um número de 0 a 5: ')))
z = 1
while y != x:
    y = int((input('Você errou tente novamente um número de 0 a 5: ')))
    z += 1
if z == 1:
    print('Parabéns você acertou! Acertou de primeira ')
else:
    print('Parabéns você acertou! Acertou em {} tentativas '.format(z))
