while True:
    try:
        celc = int(input(f'Digite a temperatura (°C): '))

        farehn = (celc * (9/5)) + 32

        print(f'Está temperatura em farenheit é: {farehn}')

        break
    except KeyboardInterrupt:
        print('\033[91m\nO usuário parou o progama\033[0m')
        break

    except ValueError:
        print('\033[91mO valor adicionado é um valor númerico.\033[0m')

    except:
        print('\033[91mO programa parou de funcionar, e o problema não foi identificado.\033[0m')
        break
