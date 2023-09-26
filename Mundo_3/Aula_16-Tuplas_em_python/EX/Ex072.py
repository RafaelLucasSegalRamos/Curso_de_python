while True:
    try:
        tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
                 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
                 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
                 'dezessete', 'dezoito', 'dezenove', 'vinte')
        while True:
            num = int(input('Digite um número entre 0 e 20: '))
            if num < 0 or num > 20:
                print('\033[91mTente novamente. O número escrito não está entre nossas opções. \033[m', end='')
            else:
                break
        print(f'Você digitou o número {tupla[num]}')
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