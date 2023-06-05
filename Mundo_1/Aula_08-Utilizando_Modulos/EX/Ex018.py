import math

while True:
    try:
        ang = int(input('Digite o ângulo: '))

        seno = math.sin(ang)
        cosseno = math.cos(ang)
        tangente = math.tan(ang)

        print(f'No ângulo {ang} tem o seno {seno:.2f}, o cosseno {cosseno:.2f} e a tangente {tangente:.2f}')

        break
    except KeyboardInterrupt:
        print('\033[91m\nO usuário parou o progama\033[0m')
        break

    except ValueError:
        print('\033[91mO valor adicionado não é um valor númerico.\033[0m')

    except:
        print('\033[91mO programa parou de funcionar, e o problema não foi identificado.\033[0m')
        break
