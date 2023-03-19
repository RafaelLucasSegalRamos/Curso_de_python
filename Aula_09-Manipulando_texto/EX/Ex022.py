

while True:
    try:
        nome = str(input('Digite seu nome completo: '))

        print(f'Seu nome completo com letra maiusculas é: {nome.upper()}')
        print(f'Seu nome completo com letra minusculas é: {nome.lower()}')
        print(f'Seu nome completa tem {len(nome.replace(" ", ""))} letras')
        print(f'Seu primeiro nome tem {len(nome.split()[0])} letras')

        break
    except KeyboardInterrupt:
        print('\033[91m\nO usuário parou o progama\033[0m')
        break

    except ValueError:
        print('\033[91mO valor adicionado não é um valor númerico possivel.\033[0m')

    except:
        print('\033[91mO programa parou de funcionar, e o problema não foi identificado.\033[0m')
        break
