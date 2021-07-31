armazenapreco = 0
totpreco = 0
cont = 0
while True:
    print('------ LOJA SUPER BARATÃO -----: ')
    nome = ' '
    preço = 0
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço:R$ '))
    cont += 1
    if cont == 1 or preço < menor:
        menor = preço
    armazenapreco += preço
    if preço > 1000:
        totpreco += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar [S/N]')).strip().upper()
    if resposta == 'N':
        break
print(f'O valor total das compras é de R$ {armazenapreco}')
print(f'Teve {totpreco} produto acima de R$ 1000')
print(f'O menor preço é de R$ {menor}')
