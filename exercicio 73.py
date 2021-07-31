classificacao = ('Flamengo','Inter','Atletico MG','SPFC','Fluminense','Gremio','Palmeiras','Santos',
        'Atletico br','bragantino','ceara','corinthians','atletico go','Bahia','Sport','Fortaleza',
        'Vasco','Goias','Coritiba','Botafogo')
print(f'Lista de times do Brasileirão 2021: {classificacao}')
print(f'Os 5 primeiros colocados são: {classificacao[0:5]}')
print(f'Os 4 últimos são: {classificacao[16:20]}')
print(f'Os times em ordem alfabética são: {sorted(classificacao)}')
print(f'O chapecoense está na {classificacao.index("ceara")+1}ªposição')
