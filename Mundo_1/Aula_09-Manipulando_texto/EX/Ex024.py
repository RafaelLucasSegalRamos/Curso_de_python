while True:
    try:
        cidade = str(input('Digite o nome de sua cidade: '))

        if 'santo' in cidade or 'santa' in cidade:
            print('Na cidade que você digitou tem a palavra santo(a)')
        else:
            print('Na cidade que você digitou \033[91mnão\033[0m tem a palavra santo(a)')

        break
    except KeyboardInterrupt:
        print('\033[91m\nO usuário parou o progama\033[0m')
        break

    except ValueError:
        print('\033[91mO valor adicionado não é um valor númerico.\033[0m')

    except:
        print('\033[91mO programa parou de funcionar, e o problema não foi identificado.\033[0m')
        break
