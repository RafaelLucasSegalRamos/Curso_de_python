import math
while True:
    try:
        numero = int(input('Digite um valor que será tranformado: '))
        while True:
            esc = int(input('Digite para qual base de conversão você quer converter seu valor: '
                            '\n[1] para binário'
                            '\n[2] para octal'
                            '\n[3] para hexadecimal'
                            '\nQual escolhera: '))
            if esc == 1:
                print(f'O valor digitado transformado em binário fica: {bin(numero).replace("b", "")}')
                break
            if esc == 2:
                print(f'O valor digitado transformado em Octal fica: {oct(numero).replace("0o", "")}')
                break
            if esc == 3:
                print(f'O valor digitado transformado em Hexadecimal fica: {hex(numero).replace("0x", "")}')
                break

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