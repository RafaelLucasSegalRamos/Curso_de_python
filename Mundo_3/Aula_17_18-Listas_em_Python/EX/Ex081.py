while True:
    try:
        lista_num = []
        while True:
            lista_num.append(int(input('Digite um valor: ')))
            while True:
                continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
                if continuar in 'SN':
                    break
                else:
                    print('\033[91mTente novamente. ', end='')
            if continuar == 'N':
                break
        print(f'Você digitou {len(lista_num)} elementos.')
        lista_num.sort(reverse=True)
        print(f'Os valores em ordem decrescente são {lista_num}')
        if 5 in lista_num:
            print('O valor 5 faz parte da lista!')
        else:
            print('O valor 5 não foi encontrado na lista!')
        break

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
