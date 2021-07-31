r1 = float(input('Digite o valor do Primeiro Segmento: '))
r2 = float(input('Digite o valor do Segundo Segmento: '))
r3 = float(input('Digite o valor do Terceiro Segmento: '))
if r1 < r2+r3 and r2< r1+r3 and r3 < r1+r2:
    print('Os segmentos acima podem formar triângulo')
    if r1 == r2 == r3:
        print('Forma um triângulo Equilátero')
    elif r1 != r2 != r3 != r1:
        print('Forma um triângulo Escaleno')
    else:
        print('Forma um triângulo Isóceles')
else:
    print('Os segmentos acima não podem formar triângulo')