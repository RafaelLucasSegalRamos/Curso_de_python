while True:
    try:
        lista_num = []
        c = 1

        for c in range(0, 5):
            num = int(input(f'Digite um valor para a {c}° posição: '))

            if c == 0 or num > lista_num[-1]:
                lista_num.append(num)
                print('Adicionado ao final da lista...')
            else:
                pos = 0
                while pos < len(lista_num):
                    if num <= lista_num[pos]:
                        lista_num.insert(pos, num)
                        print(f'Adicionado na posição {pos} da lista...')
                        break
                    pos += 1
        print(f'Os valores digitados em ordem foram {lista_num}')
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
