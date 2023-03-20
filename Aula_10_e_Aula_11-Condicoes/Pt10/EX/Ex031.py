while True:
    try:
        nome = str(input('Digite o seu nome inteiro: '))

        if 'silva' in nome.lower():
            print('No seu nome tem Silva')
        else:
            print('No seu nome \033[91mnão\033[0m tem o sobrenome Silva')

        break
    except KeyboardInterrupt:
        print('\033[91m\nO usuário parou o progama\033[0m')
        break

    except ValueError:
        print('\033[91mO valor adicionado não é um valor númerico.\033[0m')

    except:
        print('\033[91mO programa parou de funcionar, e o problema não foi identificado.\033[0m')
        break
