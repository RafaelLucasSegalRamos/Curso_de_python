while True:
    try:
        aluno = dict()
        aluno['Nome'] = str(input('Nome: ')).strip().title()
        aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
        if aluno['Média'] >= 7:
            aluno['Situação'] = 'Aprovado'
        elif 5 <= aluno['Média'] < 7:
            aluno['Situação'] = 'Recuperação'
        else:
            aluno['Situação'] = 'Reprovado'
        print('-=' * 30)
        for k, v in aluno.items():
            print(f' - {k} é igual a {v}')
        print('-=' * 30)
        while True:
            continuar2 = str(input('Deseja refazer o programa? [S/N] ')).strip().upper()[0]
            if continuar2 in 'SN':
                break
            else:
                print('\033[91mTente novamente. ', end='')
        if continuar2 == 'N':
            break

    except KeyboardInterrupt:
        print('\033[91mO usuário decidiu parar o programa.\033[m')
        break

    except Exception as erro:
        print(f'\033[91mO erro que aconteceu foi {erro}\033[m')
