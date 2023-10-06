import modulos.moedas.moedas as moe


def Ex107(p):
    print(f'A metade de {p} é {moe.metade(p)}')
    print(f'O dobro de {p} é {moe.dobro(p)}')
    print(f'Aumentando 10%, temos {moe.aumentar(p, 10)}')
    print(f'Diminuindo 13%, temos {moe.diminui(p, 13)}')


if __name__ == '__main__':
    p = float(input('Digite o preço: R$'))
    Ex107(p)
