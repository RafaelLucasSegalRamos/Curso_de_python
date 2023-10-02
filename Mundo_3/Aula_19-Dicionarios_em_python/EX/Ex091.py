import random

while True:
    try:
        jogadores = dict()
        for i in range(1, 5):
            jogadores[f'Jogador {i}'] = random.randint(1, 6)
        print('Valores sorteados:')
        for k, v in jogadores.items():
            print(f'{k} tirou {v} no dado.')
        print('-=' * 30)
        print('Ranking dos jogadores:')
        for k, v in sorted(jogadores.items(), key=lambda x: x[1], reverse=True):
            print(f'{k} tirou {v} no dado.')
        print('-=' * 30)

        while True:
            continuar2 = str(input('Deseja refazer o programa? [S/N] ')).strip().upper()[0]
            if continuar2 in 'SN':
                break
            else:
                print('\033[91mTente novamente. ', end='')
        if continuar2 == 'N':
            break

    except KeyboardInterrupt:
        print('\033[91mO usuário decidiu parar o programa.\033[m')
        break

    except Exception as erro:
        print(f'\033[91mO erro que aconteceu foi {erro}\033[m')
