import datetime
while True:
    try:
        today = str(datetime.date.today())
        anoat = int(today[0:4])
        anonas = int(input('Digite o ano em que nasceu: '))
        idade = anoat - anonas

        if 9 >= idade > 0:
            print(f'Você fara parte da seleção MIRIM na natação pois tem {idade} anos!')
        elif 14 >= idade > 9:
            print(f'Você fara parte da seleção INFANTIL na natação pois tem {idade} anos!')
        elif 19 >= idade > 14:
            print(f'Você fara parte da seleção JUNIOR na natação pois tem {idade} anos!')
        elif 20 >= idade > 19:
            print(f'Você fara parte da seleção SÊNIOR na natação pois tem {idade} anos!')
        elif idade > 20:
            print(f'Você fara parte da seleção MASTER na natação pois tem {idade} anos!')


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