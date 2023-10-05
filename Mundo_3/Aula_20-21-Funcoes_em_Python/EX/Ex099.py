from time import sleep
from random import randint


def maior(num):

    print('-=' * 30)
    print('Analisando os valores passados...')
    sleep(0.5)
    lista = []
    for c in range(0, num):
        lista.append(randint(0, 100))
    for c in lista:
        print(c, end=' ')
        sleep(0.5)
    print(f'Foram informados {len(lista)} valores ao todo.')
    print(f'O maior valor informado foi {max(lista)}.')


maior(int(input('Quantos valores você quer sortear? ').strip()))
maior(int(input('Quantos valores você quer sortear? ').strip()))
maior(int(input('Quantos valores você quer sortear? ').strip()))