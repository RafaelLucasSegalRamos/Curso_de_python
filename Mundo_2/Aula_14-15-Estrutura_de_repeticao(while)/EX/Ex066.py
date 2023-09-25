while True:
    try:
        while True:
            soma = 0
            cont = 0
            while True:
                num = int(input('Digite um número (999 para parar): '))
                if num == 999:
                    break
                soma += num
                cont += 1
            print(f'Foram digitados {cont} números, e a soma deles é {soma}')
            print(f'Entre os números digitados a média deles é {soma/cont}, o maior número foi {maior} e o menor foi {menor}')
            while True:
                resp = str(input('Quer continuar o progama? [S/N]  '))
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

    except Exception as erro:
        print(f'\033[91mO programa parou de funcionar, e o problema é {erro}.\033[0m')
        break
