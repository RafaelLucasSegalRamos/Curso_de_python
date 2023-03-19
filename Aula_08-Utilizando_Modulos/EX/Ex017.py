import math

while True:
    try:
        catop = int(input('Digite o valor do cateto oposto: '))

        caadj = int(input('Digite o valor do cateto adjacente: '))

        hipo = math.hypot(catop, caadj)

        print(f'O valor da hipotenusa deste triângulo é \033[94m{hipo}')

        break
    except KeyboardInterrupt:
        print('\033[91m\nO usuário parou o progama\033[0m')
        break

    except ValueError:
        print('\033[91mO valor adicionado não é um valor númerico.\033[0m')

    except:
        print('\033[91mO programa parou de funcionar, e o problema não foi identificado.\033[0m')
        break
