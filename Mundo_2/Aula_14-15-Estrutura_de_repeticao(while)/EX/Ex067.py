while True:
    try:
        while True:
            num = int(input('Digite um valor para se fazer uma tabuada: '))

            if num < 0:
                print('\033[91mO valor digitado é negativo\033[0m')
                break

            for c in range(0, 11):
                print(f'\033[34m{num}\033[0m * \033[96m{c}\033[0m = {num*c}')
            break


    except ValueError:
        print('\033[91mO valor digitado não é um inteiro\033[0m')

    except KeyboardInterrupt:
        print('\033[91mO usuário interrompeu o programa.\033[0m')
        break

    except:
        print('\033[91mOcorreu um problema no programa\033[0m')