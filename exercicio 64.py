n = 0
soma = 0
n1 = 0
while n != 999:
    n = int(input('Digite um número: '))
    n1 += 1
    soma += n
print('A soma dos números digitados é {} '.format(soma-999))
print('Foram digitados {} números'.format(n1-1))
