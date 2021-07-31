Valorcasa = float(input('Qual o valor da casa ? R$'))
salariocomprador = float(input('Qual o salário do comprador ? R$'))
anos = int(input('Em quantos anos ele pagará a casa? '))
prestacao = Valorcasa / (anos * 12)
minimo = 0.3 * salariocomprador
print('Para para uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(Valorcasa, anos, prestacao))
if minimo <= prestacao:
    print('Empréstimo negado!')
else:
    print('Empréstimo Aprovado!')
