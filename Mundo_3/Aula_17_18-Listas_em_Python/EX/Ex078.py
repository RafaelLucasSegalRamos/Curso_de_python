while True:
    try:
        lista_num = []
        for c in range(0, 5):
            lista_num.append(int(input(f'Digite um valor para a {c}° posição: ')))
        print(f'Você digitou os valores {lista_num}')
        for c in range(0, 5):
            if c == 0:
                maior = menor = lista_num[c]
                pos_menor = pos_maior = c
            else:
                if lista_num[c] > maior:
                    maior = lista_num[c]
                    pos_maior = c
                if lista_num[c] < menor:
                    menor = lista_num[c]
                    pos_menor = c
        print(f'O maior valor digitado foi {maior} nas posição {pos_maior}')
        print(f'O menor valor digitado foi {menor} na posição {pos_menor}')

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