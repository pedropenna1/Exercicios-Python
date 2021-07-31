valor1 =int(input('Digite o primeiro valor: '))
valor2 =int(input('Digite o segundo valor: '))
n = 0
maiorvalor = 0
while n!= 5:
    print(''' 
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos Números
        [5] Sair do programa 
    ''')
    n = int(input('Digite sua opção: '))
    if n == 1:
        print('A Soma entre {} e {} é {}'.format(valor1,valor2,valor1+valor2))
    elif n == 2:
        print('A Multiplicação entre {} e {} é {}'.format(valor1,valor2,valor1*valor2))
    elif n == 3:
        if valor1 > valor2:
            maiorvalor = valor1
        else:
            maiorvalor = valor2
        print('O maior valor entre {} e {} é {}'.format(valor1,valor2,maiorvalor))
    elif n == 4:
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))
    else:
        print('Opção inválida, tente denovo!')
print('Fim do programa')
