numero = int(input('Digite um número inteiro: '))
print('''Escolha as bases para conversão:
[1] : Conversão para binário 
[2] : Conversão para Octal
[3] : Conversão para Hexadecimal''')
opcao = int(input('Qual conversão deseja fazer? Digite sua opção:'))
if(opcao == 1):
    print('O número inteiro {} em binário é {}'.format(numero,bin(numero)[2:]))
elif(opcao == 2):
    print('O número inteiro {} em octal é {}'.format(numero,oct(numero)[2:]))
elif(opcao == 3):
    print('O número inteiro {} em Hexadecimal é {}'.format(numero,hex(numero)[2:]))
else:
    print('Não existe essa opção, iniciar novamente!')