
while True:
    try:
        n1 = float(input('Digite a primeira nota do aluno: '))
        n2 = float(input('Digite a segunda nota do aluno: '))

        m = (n1+n2)/2

        if 7.0 <= m <= 10:
            print(f'\033[32mParabéns! Sua média final foi {m}, e por isso você foi APROVADO\033[m')
        elif 5 <= m < 7:
            print(f'Ops! Sua média final foi {m}, por isso você ficou de RECUPERAÇÃO.')
        elif 0 <= m < 5:
            print(f'\033[31mEssa não! Sua média final foi {m}, por isso você foi REPROVADO.\033[m')
        else:
            print('\033[31mEssa não é uma nota possivel.\033[m')

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