def leiadinheiro(n):
    n = input('Digite um preço: R$').replace(',', '')
    while n.isnumeric() is False:
        print(f'\033[31mERRO: "{n}" é um preço inválido!\033[m')
        n = input('Digite um preço: R$')
    else:
        return int(n)
