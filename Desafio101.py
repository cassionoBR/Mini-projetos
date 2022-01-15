def voto(num):
    from datetime import datetime
    idade = datetime.today().year - nascimento
    if idade < 16:
        return f'Com {idade} anos: idade insuficiente para votar!'
    if 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: Voto opcional!'
    else:
        return f'Com {idade} anos: Voto obrigatório!'


print('==' * 20)
nascimento = int(input('Em que ano você nasceu? '))
print(voto(nascimento))
