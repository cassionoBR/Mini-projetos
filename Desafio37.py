num = int(input('Digite um número inteiro: '))
print('''Qual será a base conversão:
[1] - Binário
[2] - Octal
[3] - Hexadecímal''')
opcao = int(input('Digite sua opção: '))
if opcao == 1:
    print('O número {} convertido para binário é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O número {} convertido para octal é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O número {} convertido para hexadecimal é {}'.format(num, hex(num) [2:]))
else:
    print('Opção inválida. Tente novamente!')