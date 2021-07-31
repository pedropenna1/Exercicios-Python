palavras = ('Aprender','Conhecer','Organizar')
for p in palavras:
    print(f'\nNa Palavra {p} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra},',end='')
