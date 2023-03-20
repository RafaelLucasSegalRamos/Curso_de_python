
while True:
    try:
        salario = float(input('Digite seu salário: '))

        if salario > 1250.00:
            aumento = salario + (salario*0.10)
            print(f'\033[36mParabéns, você recebeu um aumento de 10% e por isso seu salário agora é de {aumento}')
        else:
            aumento = salario + (salario * 0.15)
            print(f'\033[32mParabéns, você recebeu um aumento de 15% e por isso seu salário agora é de {aumento}')
        break
    except KeyboardInterrupt:
        print('\033[91m\nO usuário parou o progama\033[0m')
        break

    except ValueError:
        print('\033[91mO valor adicionado não é um valor númerico.\033[0m')

    except:
        print('\033[91mO programa parou de funcionar, e o problema não foi identificado.\033[0m')
        break
