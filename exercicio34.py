x = float(input('Qual salário do funcionário? '))
if x>1250:
    y = 0.1*x
    print('Você terá um aumento de R$ {:2f} '.format(y))
    print('Portanto seu novo salário integral é de R$ {}'.format(x+y))
else:
    z = 0.15*x
    print('Você terá um aumento de R$ {:2f} '.format(z))
    print('Portanto seu novo salário integral é de R$ {}'.format(x + z))
