x = int(input('Digite o primeiro número inteiro: '))
y = int(input('Digite o segundo número inteiro: '))
z = int(input('Digite o terceiro número inteiro: '))
menor = x
if y<x and y<z:
    menor = y
if z<x and z<y:
    menor = z
maior = x
if y>x and y>z:
    maior = y
if z>x and z>y:
    maior = z
print('O menor número digitado é: {}'.format(menor))
print('O maior número digitado é: {}'.format(maior))
