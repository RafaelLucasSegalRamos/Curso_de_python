import modulos.moedas.moedas as moe


def Ex110(valor):
    moe.resumo(valor, 80, 35)


if __name__ == '__main__':
    valor = float(input('Digite o preço: R$'))
    Ex110(valor)