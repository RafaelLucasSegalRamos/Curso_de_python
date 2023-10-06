import modulos.moedas.moedas as moe

def Ex109(p):
    print(f'A metade de {p} é {moe.metade(p, True)}')
    print(f'O dobro de {p} é {moe.moedas.dobro(p, True)}')
    print(f'Aumentando 10%, temos {moe.moedas.aumentar(p, 10, True)}')
    print(f'Diminuindo 13%, temos {moe.moedas.diminui(p, 13, True)}')


if __name__ == '__main__':
    p = float(input('Digite o preço: R$'))
    Ex109(p)
