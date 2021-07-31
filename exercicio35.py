r1 = float(input('Digite o valor do Primeiro Segmento: '))
r2 = float(input('Digite o valor do Segundo Segmento: '))
r3 = float(input('Digite o valor do Terceiro Segmento: '))
if r1 < r2+r3 and r2< r1+r3 and r3 < r1+r2:
    print('Os segmnetos acima podem formar triângulo')
else:
    print('Os segmnetos acima não podem formar triângulo')