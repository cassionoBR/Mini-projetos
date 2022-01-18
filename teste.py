def menu(msg, f=False):
    mensagem = msg
    if f:
        mensagem = msg.upper()
    print('===' * 20)
    print(f'{mensagem}'.center(60))
    print('===' * 20)


def M_arquivo(n='', i=''):
    arquivo = open('README.md.txt', 'r')
    conteudo = arquivo.readlines()
    conteudo.append(f'{n} {i}\n')

    
    arquivo = open('README.md.txt', 'w')
    arquivo.writelines(conteudo)
    arquivo.close()


def cadastro():
    menu('novo cadastro', True)
    cont = 0
    while True:
        cadastro = dict()
        nome = str(input('Nome: ')).strip()
        for c in nome:
            num = '0123456789*/-+=)({}!@#$%&.,<>:_?^~"'
            if c in num:
                print('\033[31mErro! Informe um nome pessoal válido(A-Z,a-z).\033[m')
                nome = str(input('Nome: ')).strip()
            else:
                cadastro['Nome: '] = nome
        try:
            idade = int(input('Idade: '))
        except(TypeError, ValueError, KeyboardInterrupt):
            print('\033[31mERRO! por favor, digite um número inteiro válido.\033[m')
        else:
            cadastro['Idade: '] = idade
        print(f'Novo registro de {cadastro["Nome: "]} adicionado.')
        M_arquivo(cadastro['Nome: '], cadastro['Idade: '])
        cadastro.clear
        cont += 1
        break
        

def leia_dados():
    arquivo = open('README.md.txt', 'r')
    ler = arquivo.readlines()
    for c in ler:
        print(c, end='')
    arquivo.close


menu('Menu principal')
cadastro()
leia_dados()