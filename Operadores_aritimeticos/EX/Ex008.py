while True:
    try:
        metro = int(input('Digite um valor em metros para ser tranformado: '))

        cm = metro * 100
        mm = metro * 1000

        print(f'{metro} em metros, é igual a {cm} em centimetros, e igual a {mm} em milimetros.')
        break
    except KeyboardInterrupt:
        print('\033[91mO usuário parou o progama\033[0m')
        break

    except ValueError:
        print('\033[91mO valor digitado não é um número inteiro!\033[0m')

    except:
        print('\033[91mOcorreu algum erro\033[0m')

