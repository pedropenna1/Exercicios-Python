from random import randint

num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
numeros = print(f'Os números sorteados são {num}')
print(f'O Maior valor é {max(num)} e o Menor é {min(num)}')
