num = n = s = 0
while n != 999:
    n = int(input('Digite um número ou 999 para parar: '))
    if n == 999:
        break
    s += n
    num += 1
#print('A soma vale {} '.format(s))
print(f'A soma vale {s}')
print(f'Foram digitados {num} números')
