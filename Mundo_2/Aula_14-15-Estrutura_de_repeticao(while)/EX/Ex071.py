# nice

while True:
    try:
        cont_200 = cont_100 = cont_50 = cont_20 = cont_10 = cont_5 = cont_2 = cont_1 = 0
        while True:
            while True:
                valor = int(input('Digite um valor: R$'))
                if valor < 0:
                    print('\033[91mO valor não pode ser negativo.\033[0m')
                else:
                    break
            while True:
                if valor >= 200:
                    cont_200 += 1
                    valor -= 200
                elif valor >= 100:
                    cont_100 += 1
                    valor -= 100
                elif valor >= 50:
                    cont_50 += 1
                    valor -= 50
                elif valor >= 20:
                    cont_20 += 1
                    valor -= 20
                elif valor >= 10:
                    cont_10 += 1
                    valor -= 10
                elif valor >= 5:
                    cont_5 += 1
                    valor -= 5
                elif valor >= 2:
                    cont_2 += 1
                    valor -= 2
                elif valor >= 1:
                    cont_1 += 1
                    valor -= 1
                else:
                    break
            print(f'Notas de 200: {cont_200}')
            print(f'Notas de 100: {cont_100}')
            print(f'Notas de 50: {cont_50}')
            print(f'Notas de 20: {cont_20}')
            print(f'Notas de 10: {cont_10}')
            print(f'Notas de 5: {cont_5}')
            print(f'Notas de 2: {cont_2}')
            print(f'Notas de 1 : {cont_1}')
            while True:
                resp = str(input('Quer continuar o progama? [S/N]  '))[0]
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
