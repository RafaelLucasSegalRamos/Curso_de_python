
while True:
    try:
        nome = str(input('Digite um nome completo: '))

        nome = nome.split()

        print(f'O seu primeiro nome é {nome[0]} e seu ultimo é {nome[len(nome)-1]}')

        break
    except KeyboardInterrupt:
        print('\033[91m\nO usuário parou o progama\033[0m')
        break

    except ValueError:
        print('\033[91mO valor adicionado não é um valor númerico.\033[0m')

    except:
        print('\033[91mO programa parou de funcionar, e o problema não foi identificado.\033[0m')
        break
