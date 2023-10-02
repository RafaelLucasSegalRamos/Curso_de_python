while True:
    try:
        pessoas = list()
        dados = dict()
        soma = 0

        while True:
            dados['nome'] = str(input('Nome: ')).strip().title()
            dados['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
            while dados['sexo'] not in 'MF':
                print('\033[91mTente novamente. \033[0m', end='')
                dados['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
            dados['idade'] = int(input('Idade: '))
            soma += dados['idade']
            pessoas.append(dados.copy())
            dados.clear()
            while True:
                continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
                if continuar in 'SN':
                    break
                else:
                    print('\033[91mTente novamente. ', end='')
            if continuar == 'N':
                break

        print(f'\033[92mForam cadastradas {len(pessoas)} pessoas.')
        print(f'A média de idade é de {soma / len(pessoas):.2f} anos.')
        print(f'As mulheres cadastradas foram: ', end='')
        for p in pessoas:
            if p['sexo'] == 'F':
                print(f'{p["nome"]} ', end='')
        print()
        print(f'As pessoas com idade acima da média são: ', end='')
        for p in pessoas:
            if p['idade'] > soma / len(pessoas):
                print(f'{p["nome"]} ', end='')
        print('\033[m')
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
