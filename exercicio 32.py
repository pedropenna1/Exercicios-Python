x = int(input('Digite o ano que quer saber: '))
y = x%4
if y == 0 and x%100 !=0 or x%400 == 0:
    print('O ano de {} é bissexto'.format(x))
else:
    print('O ano de {} não é bissexto '.format(x))