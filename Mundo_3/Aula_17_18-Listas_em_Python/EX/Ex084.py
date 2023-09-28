while True:
    try:
        lista_pessoas = []
        dados = []

        while True:
            dados.append(str(input('Nome: ')).strip().title())
            dados.append(float(input('Peso: ')))
            lista_pessoas.append(dados[:])
            dados.clear()

            while True:
                continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
                if continuar in 'SN':
                    break
                else:
                    print('\033[91mTente novamente. ', end='')
            if continuar == 'N':
                break

        print(f'Foram cadastradas {len(lista_pessoas)} pessoas.')
        print("Lista das pessoas mais pesadas (acima de 100KG): ", end='')
        for pessoa in lista_pessoas:
            if pessoa[1] > 100:
                print(f'{pessoa[0]}', end=' ')
        print('')
        print("Lista das pessoas mais leves (abaixo de 70KG): ", end='')
        for pessoa in lista_pessoas:
            if pessoa[1] < 70:
                print(f'{pessoa[0]}', end=' ')
        print('')



        while True:
            continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
            if continuar in 'SN':
                break
            else:
                print('\033[91mTente novamente. ', end='')
        if continuar == 'N':
            break

    except KeyboardInterrupt:
        print('\033[91mO usuário decidiu parar o programa.\033[m')
        break
    except Exception as erro:
        print(f'\033[91mO erro que aconteceu foi {erro}\033[m')
