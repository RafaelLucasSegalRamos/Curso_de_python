import random
while True:
    try:
        soteados = (random.randint(0, 10), random.randint(0, 10), random.randint(0, 10), random.randint(0, 10),
                    random.randint(0, 10))
        for pos,c in enumerate(soteados):
            if pos == 0:
                maior = c
                menor = c
            else:
                if c > maior:
                    maior = c
                if c < menor:
                    menor = c
        print(f'Os números sorteados foram: {soteados}')
        print(f'O maior número sorteado foi {maior}')
        print(f'O menor número sorteado foi {menor}')

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