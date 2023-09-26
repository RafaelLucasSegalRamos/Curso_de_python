while True:
    try:
        tupla = (str(input('Digite um produto: ')),
                    float(input('Digite o preço do produto: ')),
                    str(input('Digite um produto: ')),
                    float(input('Digite o preço do produto: ')),
                    str(input('Digite um produto: ')),
                    float(input('Digite o preço do produto: ')),
                    str(input('Digite um produto: ')),
                    float(input('Digite o preço do produto: ')))
        print(f'Você digitou os valores {tupla}')
        print('-'*40)
        print(f'{"LISTAGEM DE PREÇOS":^40}')
        print('-'*40)
        for i in range(0, len(tupla), 2):
            print(f'{tupla[i]:.<30}R${tupla[i+1]:>7.2f}')
        print('-'*40)




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