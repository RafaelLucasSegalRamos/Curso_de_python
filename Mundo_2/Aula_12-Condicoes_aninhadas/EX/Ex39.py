import datetime
while True:
    try:
        anonas = int(input('Digite quando você nasceu: '))
        data = str(datetime.date.today())
        anoagr = data[0:4]
        idade = int(anoagr) - anonas

        if idade < 18:
            print(f'Você tem {idade}, ainda é muito novo para se alistar no exercito, você ainda precisa esperar {18-idade} anos')
        elif idade == 18:
            print(f'Você tem {idade}, já é hora de você se alistar no exercito!')
        else:
            print(f'Você tem {idade}, já passou da hora de você se alistar no exercito! Você tinha que ter se alistado {idade-18} anos atrás')
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