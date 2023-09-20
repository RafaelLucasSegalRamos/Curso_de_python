while True:
    try:
        while True:
            while True:
                sexo = str(input('\033[97mDigite seu sexo [M/F]: ')).lower()
                if sexo in 'mf':
                    break
                else:
                    print('\033[91mSexo inválido, tente novamente.')
            print('\033[92mSexo {} registrado com sucesso.'.format(sexo))
            while True:
                resp = str(input('\033[95mQuer continuar verificandos dados?[S/N]: ')).lower()
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
