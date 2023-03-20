while True:
    try:
        num = float(input('Digite um número: '))

        if num % 2 == 1:
            print('\033[33mEste é um número IMPAR')
        else:
            print('\033[97mEste é um número PAR')

        break
    except KeyboardInterrupt:
        print('\033[91m\nO usuário parou o progama\033[0m')
        break

    except ValueError:
        print('\033[91mO valor adicionado não é um valor númerico.\033[0m')

    except:
        print('\033[91mO programa parou de funcionar, e o problema não foi identificado.\033[0m')
        break
