from time import sleep

while True:
    try:
        while True:
            fact = 1
            num = int(input('Digite um número para calcular seu fatorial: '))
            num_ant = num
            print(f'Calculando {num}! = ')
            sleep(0.5)
            while num != 1:
                if (num-1) % 10 == 0:
                    print(f'{num} x ', flush=True)
                else:
                    print(f'{num} x ', end='')
                fact *= num
                num -= 1
                if num <= 19:
                    sleep(0.5)
            print(f'1 = {fact}')

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
