while True:
    try:
        lista_num = [[], [], []]
        for i in range(0, 3):
            for j in range(0, 3):
                lista_num[i].append(int(input(f'Digite um valor para [{i}, {j}]: ')))

        for i in range(0, 3):
            for j in range(0, 3):
                print(f'[{lista_num[i][j]:^5}]', end='')
            print()
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
