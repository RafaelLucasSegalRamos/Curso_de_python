import datetime
while True:
    try:
        height = int(input('Digite sua altura em cm: '))
        peso = int(input('Digite seu peso: '))

        imc = peso/((height/100)**2)

        if imc < 18.5:
            print('Seu IMC é baixo demais!!')
        elif 18.5 < imc < 25:
            print('Você tem o peso ideial!')
        elif 25 < imc < 30:
            print('Você está com sobrepeso.')
        elif 30 < imc < 40:
            print('Você está obeso!')
        elif 40 < imc:
            print('Você tem obesidade morbida.')

        while True:
            resp = str(input('Quer continuar? [S/N] ')).upper()
            if resp in 'SN':
                break
            else:
                print('\033[31mEstá não é uma das respostas possiveis!!\033[m')
        if resp in 'N':
            break

    except KeyboardInterrupt:
        print('\033[31mO usuário interrompeu o progama.\033[m')
        break
    except ValueError:
        print('\033[31mEste valor não condiz com o que foi pedido.\033[m')
    except:
        print('\033[31mOcorreu um erro não identificado.\033[m')