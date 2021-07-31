print('{:=^40}'.format(' Lojas Penna '))
pagamento = float(input('Qual valor das compras? R$: '))
print('''Seu pagamento será em:
[1] : à vista, dinheiro ou cheque.
[2] : à vista no cartão.
[3] : 2x no cartão.
[4] 3x ou mais no cartão.''')
opcao = int(input('Digite a sua opção de pagamento: '))
if opcao == 1:
    print('Seu pagamento de R${} recebeu uma redução de 10% e você pagará R${}'.format(pagamento, pagamento-(pagamento*0.1)))
elif opcao == 2:
    print('Seu pagamento de R${} recebeu uma redução de 5% e você pagará R${}'.format(pagamento, pagamento-(pagamento*0.05)))
elif opcao == 3:
    print('Seu pagamento será normal no valor de R$ {}'.format(pagamento))
elif opcao == 4:
    print('Seu pagamento de R${} recebeu um juros de 20% e você pagará R${}'.format(pagamento,(pagamento+(pagamento*0.20))))
