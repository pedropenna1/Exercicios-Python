from math import factorial
num = int(input('Digite um número inteiro '))
c = num
print('Calulando {} ! = '.format(num),end=' ')
f = factorial(num)
while c > 0:
    print('{}'.format(c), end=' ')
    print('x' if c > 1 else ' = ',end=' ')
    c -= 1
print('{}'.format(f),end=' ')