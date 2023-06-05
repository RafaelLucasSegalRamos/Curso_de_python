while True:
    try:
        kime = int(input('Digite quantos quilotros terá está viagem: '))

        if kime <= 200:
            print(f'\033[35mO custo da passagem será de {kime*0.5}')
        else:
            print(f'\033[36mO custo desta viagem será de {kime*0.45}')

        break
    except KeyboardInterrupt:
        print('\033[91m\nO usuário parou o progama\033[0m')
        break

    except ValueError:
        print('\033[91mO valor adicionado não é um valor númerico.\033[0m')

    except:
        print('\033[91mO programa parou de funcionar, e o problema não foi identificado.\033[0m')
        break
