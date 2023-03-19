import math

while True:
    try:
        real = float(input('Digite um valor Real(Float): '))

        inteiro = math.trunc(real)

        print(f'A parte inteira deste numero é: {inteiro}')
        break
    except KeyboardInterrupt:
        print('\033[91m\nO usuário parou o progama\033[0m')
        break

    except ValueError:
        print('\033[91mO valor adicionado não é um valor númerico.\033[0m')

    except:
        print('\033[91mO programa parou de funcionar, e o problema não foi identificado.\033[0m')
        break
