n = 'S' .upper()
s = 0
n1 = 0
soma = 0
maior = 0
menor = 0
while not n == 'N':
    s = int(input('Digite um número: '))
    n = str(input('Quer continuar [S/N]')).upper()
    n1 += 1
    soma += s
    if n1 == 1:
        maior = menor = s
    else:
        if s > maior:
            maior = s
        if s < menor:
            menor = s
print('A média dos números digitados é {} '.format(soma/n1))
print('O maior numero digitado foi {}  e o menor foi {}'.format(maior,menor))


