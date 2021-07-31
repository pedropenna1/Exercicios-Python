kmpercorrido = float(input('Qual a quantidade de km percorrido pelo veículo alugado? '))
dias = float(input('Quantos dias o veículo ficou alugado? '))
preco = (kmpercorrido*0.15)+(dias*60)
print('O valor a pagar pelo aluguel do veiculo é de: RS{:.2f}'.format(preco))
