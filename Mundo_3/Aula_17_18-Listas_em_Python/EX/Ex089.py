import random

while True:
    try:
        alunos = []

        while True:
            aluno = str(input('Nome do aluno: ')).strip().title()
            n1 = float(input('Nota 1: '))
            n2 = float(input('Nota 2: '))
            if aluno != '':
                alunos.append([aluno, n1, n2])
            else:
                print('\033[91mTente novamente. ', end='')
                continue
            while True:
                resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
                if resp in "NS":
                    break
                else:
                    print('\033[91mTente novamente. \033[0m', end='')
            if resp == 'N':
                break
        for i in range(0, len(alunos)):
            print(f'{i+1}º aluno: {alunos[i][0]} teve como média {(alunos[i][1] + alunos[i][2]) / 2:.2f}')

        while True:
            resp2 = str(input('Deseja ver as notas de algum aluno? [S/N] ')).strip().upper()[0]
            if resp2 in 'SN':
                break
            else:
                print('\033[91mTente novamente. \033[0m', end='')
        if resp2 == 'S':
            while True:
                nome = str(input('Escreva o nome do aluno para ver suas notas: ')).strip().title()
                for i in range(0, len(alunos)):
                    if alunos[i][0] == nome:
                        print(f'As notas de {alunos[i][0]} foram {alunos[i][1]} e {alunos[i][2]}')
                        break
                    else:
                        print('\033[91mTente novamente. \033[0m', end='')

                while True:
                    resp2 = str(input('Deseja ver as notas de outro aluno? [S/N] ')).strip().upper()[0]
                    if resp2 in 'SN':
                        break
                    else:
                        print('\033[91mTente novamente. \033[0m', end='')
                if resp2 == 'N':
                    break
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
