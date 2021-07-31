somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = 0
totmulher20 = 0
for n in range (1, 5):
    print(('------ {}ª pessoa -----: '.format(n)))
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a Idade: '))
    sexo = str(input('Digite o sexo [M/F]')).strip()
    somaidade = somaidade+idade
    if n == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade/4
print('A média da idade do grupo é de {}'.format(mediaidade))
print('O Homem mais velho tem {} anos e seu nome é {}'.format(maioridadehomem,nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))