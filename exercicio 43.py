peso = float(input('Qual é o seu peso em Kilos?  '))
altura = float(input('Qual é a sua altura em metros: '))
IMC = peso/(altura**2)
print('Seu IMC é de {:.1f} '.format(IMC))
if IMC < 18.5:
    print('Abaixo do peso')
elif 18.5 <= IMC < 25:
    print('Peso Ideal')
elif 25 <= IMC < 30:
    print('Sobrepeso')
elif 30 <= IMC < 40:
    print('Obesidade')
elif IMC > 40:
    print('Obesidade Mórbida')
