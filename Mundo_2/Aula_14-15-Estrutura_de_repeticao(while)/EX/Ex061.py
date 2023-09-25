while True:
    try:
        while True:
            termo = 0
            num = float(input('Digite o primeiro termo da PA: '))
            razao = int(input('Digite a razão da PA: '))
            termos = int(input('Digite quantos termos você quer ver: '))
            num_ant = num
            print(f'Calculando {num}! = ')
            if razao == 0:
                print('\033[91mNão é uma PA.')
            else:
                while termos > termo:
                    termo += 1
                    print(f'O {termo}º termo é {num} + {razao} = {num+razao}')
                    num += razao
            print(f'\033[92m\nO resultado final é {num}\033[0m')

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
