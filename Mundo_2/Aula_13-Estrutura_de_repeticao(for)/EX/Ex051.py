from time import sleep
pf = 0

while True:
    try:
        while True:
            pa1 = int(input('\033[97mDigite o primeiro termo da PA: '))
            r = int(input('Digite a razão da PA: '))
            if r == 0:
                print('\033[91mNão é uma PA.')
            else:
                for i in range(1, 11):
                    print(f'\033[92m{pa1}', end=", ")
                    pa1 += r
            print(f'\033[92m\nO resultado final é {pa1}')
            while True:
                resp = str(input('\033[95mQuer continuar vendo PAs?[S/N]: ')).lower()
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
