import modulos.moedas.moedas as moe
import modulos.dado as dad


def Ex112(valor):
    moe.resumo(valor, 80, 35)


if __name__ == '__main__':
    valor = dad.leiaDinheiro()
    Ex112(valor)