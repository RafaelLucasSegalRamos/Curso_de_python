while True:
    try:
        sala = float(input('Escreva o salário do funcionario, a receber o aumento: R$'))

        aumen = float(input('Escreva a porcentagem que será aumentada do funcionario,'
                            ' que vai receber o aumento: '))

        salafinal = sala + (sala * (aumen/100))

        print(f'O salário final deste funcionário foi: R${salafinal:.2f}')
        break
    except KeyboardInterrupt:
        print('\033[91m\nO usuário parou o progama\033[0m')
        break

    except ValueError:
        print('\033[91mO valor adicionado é um valor númerico.\033[0m')

    except:
        print('\033[91mO programa parou de funcionar, e o problema não foi identificado.\033[0m')
