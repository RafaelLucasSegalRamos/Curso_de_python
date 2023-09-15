from time import sleep
while True:
    try:
        print('a')
        break
    except KeyboardInterrupt:
        print('\033[91m\nO usuário interrompeu o progama.')
        break

    except:
        print('\033[91m\nOcorreu um erro não identificado.')
