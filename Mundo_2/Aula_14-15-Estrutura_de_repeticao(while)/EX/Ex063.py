while True:
    try:
        while True:
            i = 0
            t1 = 1
            t2 = 0
            nSeq = int(input('Digite quantos termos da sequência de Fibonacci você quer ver: '))

            if nSeq <= 0:
                print('\033[91mO valor não é um valor possivel.\033[0m')
            else:
                while i < nSeq:
                    print(f'\033[92m{t1}', end=', ')
                    t3 = t1 + t2
                    t2 = t1
                    t1 = t3
                    i += 1
                print('\033[0mFIM')
            while True:
                resp = str(input('Quer continuar? [S/N]  '))
                if resp.upper() in 'S':
                    break
                elif resp.upper() in 'N':
                    break
                else:
                    print(f'\033[91mA resposta {resp}, não é uma das opções possiveis!\033[0m')
            if resp.upper() in 'N':
                break
        break
    except KeyboardInterrupt:
        print('\033[91m\nO usuário parou o progama\033[0m')
        break

    except ValueError:
        print('\033[91mO valor adicionado não é um valor númerico possivel.\033[0m')

    except:
        print('\033[91mO programa parou de funcionar, e o problema não foi identificado.\033[0m')
        break
