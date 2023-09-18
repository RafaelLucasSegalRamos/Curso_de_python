# Descobrindo se um número é primo:

while True:
    try:
        while True:
            num = int(input('\033[97mDigite um número: '))
            if num == 0 or num == 1:
                print('\033[91mNão é um número primo.')
            elif num == 2:
                print('\033[92mÉ um número primo.')
            else:
                for i in range(2, num):
                    if num % i == 0:
                        print('\033[91mNão é um número primo.')
                        break
                else:
                    print('\033[92mÉ um número primo.')

            while True:
                resp = str(input('\033[95mQuer continuar vendo números primos?[S/N]: ')).lower()
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
