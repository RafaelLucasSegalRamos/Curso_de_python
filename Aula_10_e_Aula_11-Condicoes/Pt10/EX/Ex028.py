from random import randint
from time import sleep

while True:
    try:
        while True:
            numusu = int(input('Digite um número entre 1 e 5 para tentar acertar o número do progama: '))
            nummaq = randint(1, 5)

            if numusu == nummaq:
                print(f'\033[94mParabéns!! Você acertou o numero! Pois o numero {numusu} é igual ao {nummaq}, '
                      f'que foi o número que a maquina escolheu\033[0m')
            else:
                print(f'\033[31mEssa não!!\033[91m Você errou o numero! Pois o numero {numusu} é diferente {nummaq}, '
                      f'que foi o número que a maquina escolheu\033[0m')
            while True:
                resp = str(input('Quer continuar? [S/N]  '))
                if resp.upper() in 'S':
                    break
                elif resp.upper() in 'N':
                    break
                else:
                    print(f'\033[91mA resposta {resp}, não é uma das opções possiveis!\033[0m')
            if resp.upper() in 'N':
                break
        break
    except KeyboardInterrupt:
        print('\033[91m\nO usuário parou o progama\033[0m')
        break

    except ValueError:
        print('\033[91mO valor adicionado não é um valor númerico possivel.\033[0m')

    except:
        print('\033[91mO programa parou de funcionar, e o problema não foi identificado.\033[0m')
        break
