totidade = 0
tothomem = 0
totmulher20 = 0
while True:
    print('------ Cadastre uma pessoa -----: ')
    idade = int(input('Digite a Idade: '))
    sexo = ' '
    resposta = ' '
    while sexo not in'MF':
        sexo = str(input('Digite o sexo [M/F]')).strip().upper()
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar [S/N]')).strip().upper()
    if idade >= 18:
        totidade += 1
    if sexo in 'Mm':
        tothomem += 1
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
    if resposta == 'N':
        break
print('Tem {} pessoas maiores de 18 anos '.format(totidade))
print('Tem um total de {} Homens'.format(tothomem))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))