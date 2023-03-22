
while True:
    try:
        listan = list()

        for c in range(1, 4):
            listan.append(float(input('Digite um número: ')))
        maxi = listan[0]
        mini = listan[0]
        for i in range(0, 3):
            if listan[i] > maxi:
                maxi = listan[i]
            elif listan[i] < mini:
                mini = listan[i]
        print(f'Entre os números {listan} o maior foi {maxi}, e o menor foi {mini}')
        break
    except KeyboardInterrupt:
        print('\033[91m\nO usuário parou o progama\033[0m')
        break

    except ValueError:
        print('\033[91mO valor adicionado não é um valor númerico.\033[0m')

    except:
        print('\033[91mO programa parou de funcionar, e o problema não foi identificado.\033[0m')
        break
