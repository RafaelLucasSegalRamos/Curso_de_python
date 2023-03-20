
while True:
    try:
        velo = int(input('Digite a velocidade do carro: '))

        if velo >= 80:
            multa = velo - 80
            print(f'\033[91mVocê foi multado!! por {multa}Km a mais!\033[0m')

            multapreco = multa * 7

            print(f'\033[31mE por isso você terá que pagar R${multapreco:.2f}')
        else:
            print('\033[96mMuito bem! você tem que manter a faixa de velocidade abaixo do limite!')
        print('\033[32mSempre viaje com segurança, coloque sempre o cinto de segurança!')
        break
    except KeyboardInterrupt:
        print('\033[91m\nO usuário parou o progama\033[0m')
        break

    except ValueError:
        print('\033[91mO valor adicionado não é um valor númerico.\033[0m')

    except:
        print('\033[91mO programa parou de funcionar, e o problema não foi identificado.\033[0m')
        break
