while True:
    try:
        lista_num = []
        lista_p = []
        lista_i = []
        while True:
            num = (int(input('Digite um valor: ')))
            if num == 0:
                print('\033[91mZero é um número nulo! Não irei adicionar[m')
            elif num % 2 == 0:
                lista_p.append(num)
            else:
                lista_i.append(num)

            while True:
                continuar2 = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
                if continuar2 in 'SN':
                    break
                else:
                    print('\033[91mTente novamente. ', end='')
            if continuar2 == 'N':
                break
        print(f'Os valores pares digitados foram {lista_p}')
        print(f'Os valores ímpares digitados foram {lista_i}')

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
