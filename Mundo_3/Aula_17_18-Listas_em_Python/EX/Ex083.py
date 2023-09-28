while True:
    try:
        expr = str(input('Digite a expressão: '))
        pilha = []
        for simb in expr:
            if simb == '(':
                pilha.append('(')
            elif simb == ')':
                if len(pilha) > 0:
                    pilha.pop()
                else:
                    pilha.append(')')
                    break
        if len(pilha) == 0:
            print('Sua expressão está válida!')
            print(eval(expr))
        else:
            print('Sua expressão está errada!')



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
