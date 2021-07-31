nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
media = (nota1+nota2)/2
if media < 5:
    print('Aluno reprovado média igual a {}'.format(media))
elif 6 <= media <= 6.9:
    print('Aluno de recuperação média igual a {}'.format(media))
else:
    print('Aluno aprovado média igual a {}'.format(media))
