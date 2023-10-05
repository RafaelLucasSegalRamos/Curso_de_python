from random import randint
from time import sleep


def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    lista = []
    for c in range(0, 5):
        n = randint(1, 10)
        print(f'{n} ', end='')
        sleep(0.3)
        lista.append(n)
    print('PRONTO!')
    return lista


def somaPar(listas):
    soma = 0
    for c in listas:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {listas}, temos {soma}.')


somaPar(sorteia())
print()
somaPar(sorteia())
print()
somaPar(sorteia())
