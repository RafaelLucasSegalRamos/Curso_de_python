import random

while True:
    try:
        jogos = []
        jogos_mostrados = []

        while True:
            num_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
            if num_jogos > 0:
                break
            else:
                print('\033[91mTente novamente. ', end='')

        for i in range(0, num_jogos):
            jogos.append([random.randint(1, 60), random.randint(1, 60), random.randint(1, 60), random.randint(1, 60), random.randint(1, 60), random.randint(1, 60)])
        for i in range(0, len(jogos)):
            if not(jogos[i] in jogos_mostrados):
                jogos[i].sort()
                print(f'Jogo {i+1}: {jogos[i]}')
                jogos_mostrados.append(jogos[i])
            else:
                print(f'O jogo de número {i} já foi mostrado anteriormente. ', end='')


        while True:
            continuar2 = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
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
