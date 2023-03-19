try:
    notas = list()
    while True:
        n = str(input('Digite a nota do aluno: '))
        if n.isnumeric():
            no = int(n)
            notas.append(no)
        else:
            print(f'\033[91mO valor {n} não é numerico!\033[0m')
        while True:
            resp = str(input('Quer continuar adicionando notas? [S/N]  '))
            if resp in 'Nn':
                break
            elif resp in 'Ss':
                print('Ok, Continue adicionando.')
                break
            else:
                print('\033[91mO valor adicionado não é uma das respostas possiveis\033[0m')
        if resp in 'Nn':
            break
    nf = 0
    for c in notas:
        nf += c
    m = nf / len(notas)

    print(f'A media desse aluno é {m}, pois foram registradas {len(notas)} notas, que se somaram em {nf}')

except:
    print(f'\033[91mAlgo deu errado! ou o usuário parou o progama!')