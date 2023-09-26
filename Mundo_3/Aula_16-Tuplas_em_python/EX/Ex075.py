while True:
    try:
        tupla = (int(input('Digite um número: ')),
                    int(input('Digite outro número: ')),
                    int(input('Digite mais um número: ')),
                    int(input('Digite o último número: ')))
        print(f'Você digitou os valores {tupla}')
        print(f'O valor 9 apareceu {tupla.count(9)} vezes')
        if 3 in tupla:
            print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posição')
        else:
            print('O valor 3 não foi digitado em nenhuma posição')
        print('Os valores pares digitados foram: ', end='')
        for n in tupla:
            if n % 2 == 0:
                print(n, end=' ')
        print()


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