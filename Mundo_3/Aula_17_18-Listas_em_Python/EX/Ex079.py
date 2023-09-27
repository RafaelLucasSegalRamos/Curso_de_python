while True:
    try:
        lista_num = []
        c = 1
        while True:
            num = int(input(f'Digite um valor para a {c}° posição: '))

            if num in lista_num:
                print('\033[91mValor duplicado! Não vou adicionar...\033[m')
            else:
                lista_num.append(num)
                print('Valor adicionado com sucesso...')
                c += 1
            while True:
                continuar2 = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
                if continuar2 in 'SN':
                    break
                else:
                    print('\033[91mTente novamente. \033[0m', end='')

            if continuar2 == 'N':
                break
        lista_num.sort()
        print(f'Você digitou os valores {lista_num}')

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
