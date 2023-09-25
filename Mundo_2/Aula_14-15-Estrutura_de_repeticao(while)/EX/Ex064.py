while True:
    try:
        while True:
            soma = cont = 0
            while True:
                num = int(input('Digite um número: [999 para parar] '))
                if num == 999:
                    break
                else:
                    soma += num
                    cont += 1
            print(f'Você digitou {cont} números e a soma entre eles foi {soma}')
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
