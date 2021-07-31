from datetime import date
atual = date.today().year
nascimento = int(input('Digite o ano do nascimento: '))
idade = atual - nascimento
if idade == 18:
    print('Sua idade é {} anos'.format(idade))
    print('Deve se alistar imediatamente!')
elif idade < 18:
    print('Sua idade é {} anos'.format(idade))
    print('Não chegou a idade de alistamento ainda falta {} anos'.format(18 - idade))
    print('Seu alistamento será em {} '.format(nascimento + 18))
else:
    print('Sua idade é {} anos'.format(idade))
    print('A idade de alistamento ja passou, passou em {} anos'.format(atual - (nascimento+18)))
    print('Seu alistamento foi em {} '.format(nascimento+18))