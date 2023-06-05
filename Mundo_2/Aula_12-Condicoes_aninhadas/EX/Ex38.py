import math
while True:
    try:
        n1 = float(input('Digite um valor: '))
        n2 = float(input('Digite um outro valor: '))

        if n1 < n2:
            print(f'O segundo valor digitado , {n2}, é o maior entre os dois')
        elif n1 > n2:
            print(f'O primeiro valor digitado , {n1}, é o maior entre os dois')
        else:
            print(f'Ambos os valores são iguais, {n1} e {n2}, por isso não existe um valor maior.')
        while True:
            resp = str(input('Quer continuar? [S/N] ')).upper()
            if resp in 'SN':
                break
            else:
                print('\033[31mEstá não é uma das respostas possiveis!!\033[m')
        if resp in 'N':
            break
    except KeyboardInterrupt:
        print('\033[31mO usuário interrompeu o progama.\033[m')
        break
    except ValueError:
        print('\033[31mEste valor não condiz com o que foi pedido.\033[m')
    except:
        print('\033[31mOcorreu um erro não identificado.\033[m')