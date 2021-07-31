x = float(input('Digite a velocidade do carro em kms/hr: '))
if x>80:
    print('Multado')
    y = float(((x - 80) * 0.70))
    print('Você foi multado em:R$ {}'.format(y))
else:
    print('Tenha um bom dia! Dirija com segurança.')
