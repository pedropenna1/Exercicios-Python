from datetime import date
atual = date.today().year
ano = int(input('Digite o ano de nascimento do atleta: '))
idade = atual - ano
if idade <= 9:
    print('A idade do atleta é de {} anos'.format(idade))
    print('Sua classificação é Mirim')
elif 9 < idade <= 14:
    print('A idade do atleta é de {} anos'.format(idade))
    print('Sua classificação é Infantil')
elif 14 < idade <=19:
    print('A idade do atleta é de {} anos'.format(idade))
    print('Sua classificação é Junior')
elif 19 < idade <= 20:
    print('A idade do atleta é de {} anos'.format(idade))
    print('Sua classificação é Senior')
else:
    print('A idade do atleta é de {} anos'.format(idade))
    print('Sua classificação é Master')