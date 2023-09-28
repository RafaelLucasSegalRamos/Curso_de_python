while True:
    try:
        lista_num = [[],[]]
        while True:
            num = (int(input('Digite um valor: ')))
            if num == 0:
                print('\033[91mZero é um número nulo! Não irei adicionar[m')
            elif num % 2 == 0:
                lista_num[0].append(num)
            else:
                lista_num[1].append(num)

            while True:
                continuar2 = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
                if continuar2 in 'SN':
                    break
                else:
                    print('\033[91mTente novamente. ', end='')
            if continuar2 == 'N':
                break
        print(f'Os valores pares digitados foram {lista_num[0]}')
        print(f'Os valores ímpares digitados foram {lista_num[1]}')
        print(f'Os valores pares digitados em ordem crescente foram {sorted(lista_num[0])}')
        print(f'Os valores ímpares digitados em ordem crescente foram {sorted(lista_num[1])}')

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
