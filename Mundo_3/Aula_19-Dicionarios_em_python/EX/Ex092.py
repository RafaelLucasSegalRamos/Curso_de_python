import datetime
while True:
    try:
        pessoas = dict()
        pessoas['Nome'] = str(input('Nome: ')).strip().title()
        pessoas['idade'] = datetime.date.today().year - int(input(f'Ano de nascimento de {pessoas["Nome"]}: '))
        pessoas['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
        if pessoas['CTPS'] != 0:
            pessoas['Contratação'] = int(input('Ano de contratação: '))
            pessoas['Salário'] = float(input('Salário: R$'))
            pessoas['Aposentadoria'] = pessoas['idade'] + (35 - (datetime.date.today().year - pessoas['Contratação']))
        print('-=' * 30)
        for k, v in pessoas.items():
            print(f'{k} tem o valor {v}')
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
