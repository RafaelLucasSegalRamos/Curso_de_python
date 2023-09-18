
while True:
    try:
        while True:
            frase = str(input('\033[97mDigite uma frase: ')).replace(" ", "").lower()
            if frase == frase[::-1]:
                print('\033[92mÉ uma frase palíndroma.')
            else:
                print('\033[91mNão é uma frase palíndroma.')
            while True:
                resp = str(input('\033[95mQuer continuar vendo frase palíndromas?[S/N]: ')).lower()
                if resp in 'sn':
                    break
            if resp == 'n':
                break
        break
    except KeyboardInterrupt:
        print('\033[91m\nO usuário interrompeu o progama.')
        break

    except:
        print('\033[91m\nOcorreu um erro não identificado.')
