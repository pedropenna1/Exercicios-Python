primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
c = 1
total = 0
mais = 10
soma = 0
while mais!= 0:
    total = total + mais
    while c <= total:
        print('{}'.format(termo),end=' ')
        termo = termo + razao
        c += 1
    mais = int(input('Deseja fazer mais termos?'))
    soma += mais
print('utilizou mais {} termos '.format(soma))
print('FIM!!!!!!')
