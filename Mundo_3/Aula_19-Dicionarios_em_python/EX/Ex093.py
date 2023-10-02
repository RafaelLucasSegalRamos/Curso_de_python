while True:
    try:
        jogadores_de_futebol = dict()
        jogadores_de_futebol['Nome'] = str(input('Nome do jogador: ')).strip().title()
        jogadores_de_futebol['Partidas'] = int(input(f'Quantas partidas {jogadores_de_futebol["Nome"]} jogou? '))
        jogadores_de_futebol['Gols'] = list()
        for i in range(0, jogadores_de_futebol['Partidas']):
            jogadores_de_futebol['Gols'].append(int(input(f'Quantos gols na partida {i + 1}? ')))
        jogadores_de_futebol['Total'] = sum(jogadores_de_futebol['Gols'])
        print('-=' * 30)
        print(jogadores_de_futebol)
        print('-=' * 30)
        for k, v in jogadores_de_futebol.items():
            print(f'O campo {k} tem o valor {v}')
        print('-=' * 30)
        print(f'O jogador {jogadores_de_futebol["Nome"]} jogou {jogadores_de_futebol["Partidas"]} partidas.')
        for i, v in enumerate(jogadores_de_futebol['Gols']):
            print(f'    => Na partida {i + 1}, fez {v} gols.')
        print(f'Foi um total de {jogadores_de_futebol["Total"]} gols.')
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
