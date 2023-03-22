

while True:
    try:
        ano = int(input('Digite um ano: '))
        if ano % 4 == 0:
            print(f'{ano} é BISSEXTO')
        else:
            print(f'{ano} NÃO É BISSEXTO')


        break
    except KeyboardInterrupt:
        print('\033[91m\nO usuário parou o progama\033[0m')
        break

    except ValueError:
        print('\033[91mO valor adicionado não é um valor númerico possivel.\033[0m')

    except:
        print('\033[91mO programa parou de funcionar, e o problema não foi identificado.\033[0m')
        break
