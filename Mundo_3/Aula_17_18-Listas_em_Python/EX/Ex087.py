while True:
    try:
        lista_num = [[], [], []]
        for i in range(0, 3):
            for j in range(0, 3):
                lista_num[i].append(int(input(f'Digite um valor para [{i}, {j}]: ')))

        for i in range(0, 3):
            for j in range(0, 3):
                print(f'[{lista_num[i][j]:^7}]', end='')
            print()

        soma_par = 0
        soma_terc_col = 0

        for i in range(0, 3):
            for j in range(0, 3):
                if lista_num[i][j] % 2 == 0:
                    soma_par += lista_num[i][j]
                if j == 2:
                    soma_terc_col += lista_num[i][j]
                if j == 0 and i == 1:
                    maior_seg_lin = lista_num[i][j]
                elif i == 1 and lista_num[i][j] > maior_seg_lin:
                    maior_seg_lin = lista_num[i][j]

        print(f'A soma dos valores pares é {soma_par}')
        print(f'A soma dos valores da terceira coluna é {soma_terc_col}')
        print(f'O maior valor da segunda linha é {maior_seg_lin}')

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
