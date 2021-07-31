num1 = float(input('Digite um número: '))
num2 = float(input('Digite um número: '))
if num1 > num2:
    print('O número {:.2f} é maior que o número {:.2f}'.format(num1,num2))
elif num1 < num2:
    print('O número {:.2f} é maior que o número {:.2f}'.format(num2,num1))
else:
    print('O número {:.2f} é igual ao número {:.2f}'.format(num1,num2))
