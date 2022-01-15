times = ('Atletico-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthias',
         'Bragantino', 'Fluminense', ' America-MG', 'Atletico-GO', 'Santos',
         'Ceara', 'Internacional', 'Sao Paulo', 'Athletico-PR', 'Cuiabá',
         'Juventude', 'Gremio', 'Bahia', 'Sport', 'Chapecoense')
print(f'Os 5º PRIMEIROS colocados {times[:5]}')
print(f'Os 4º ÚLTIMOS colocados {times[-4:]}')
print(f'>>> Times em ordem alfabetica:\n{sorted(times)}')
print(f'A Chapecoense está na {times.index("Chapecoense") + 1}ª posição')