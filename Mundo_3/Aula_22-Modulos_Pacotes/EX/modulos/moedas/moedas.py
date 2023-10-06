# Ex107
def aumentar(valor, porcAumenta, format=False):
    resp = valor + (valor * porcAumenta / 100)
    if format:  # Ex109
        return moeda(resp)
    else:
        return resp


def diminui(valor, porcDiminui, format=False):
    resp = valor - (valor * porcDiminui / 100)
    if format:  # Ex109
        return moeda(resp)
    else:
        return resp


def dobro(valor, format=False):
    resp = valor * 2
    if format:  # Ex109
        return moeda(resp)
    else:
        return valor * 2


def metade(valor, format=False):
    resp = valor / 2
    if format:  # Ex109
        return moeda(resp)
    else:
        return resp


# Ex108
def moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',')


# Ex110
def resumo(valor, porcAumenta, porcDiminui):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'A metade de {moeda(valor)} é {metade(valor, True)}')
    print(f'O dobro de {moeda(valor)} é {dobro(valor, True)}')
    print(f'Aumentando {porcAumenta}%, temos {aumentar(valor, porcAumenta, True)}')
    print(f'Diminuindo {porcDiminui}%, temos {diminui(valor, porcDiminui, True)}')
