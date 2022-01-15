from random import sample
num = sample(range(11), 5)
print(f'''Os valores sorteados foram {num}
O maior valor sorteado foi {max(num)}
O menor valor sorteado foi {min(num)}''')
