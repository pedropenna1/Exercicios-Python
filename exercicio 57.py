sexo = str(input('Digite seu sexo [M/F]')).upper()
while not sexo in 'MF':
    sexo =  str(input('Dado inválido informe corretamente seu sexo [M/F]')).upper()
print('Sexo {} registrado com sucesso'.format(sexo))