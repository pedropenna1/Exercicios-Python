tupla = ('Zero','UM','DOIS','TRÊS','QUATRO','CINCO','SEIS','SETE',
        'OITO','NOVE','DEZ','ONZE','DOZE','TREZE','CATORZE','QUINZE',
        'DEZESSEIS','DEZESSETE','DEZOITO','DEZENOVE','VINTE')
while True:
    numero = int(input('Digite um número de 0 a 20: '))
    if 0 <= numero <= 20:
        break

print(f'O número que você digitou por extenso é escrito desta forma:{tupla[numero]}')
