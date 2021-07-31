from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range (1, 8):
    nasc = int(input('Digite o ano em que a {}ª pessoa nasceu: '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor +=1
print('Temos {} maiores de idade'.format(totmaior))
print('Temos {} menores de idade'.format(totmenor))