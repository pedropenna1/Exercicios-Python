n = int(input('Digite um número inteiro '))
t1 = 0
t2 = 1
print(' {}  {} '.format(t1,t2),end=' ')
cont = 3
while cont <= n:
    t3 = t2 + t1
    print(' {} '.format(t3),end=' ')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM !!!!!!')
