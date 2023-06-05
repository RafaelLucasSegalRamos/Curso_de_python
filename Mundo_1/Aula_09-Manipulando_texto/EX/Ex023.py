

while True:
    try:
        while True:
            nume = int(input('Digite um valor de 0 a 9999: '))
            if 0 <= nume <= 9999:
                break
            else:
                print('\033[91mO valor digitado é menor que 0, ou maior que 9999')
        nume = str(nume)
        print(f'O número {nume} é dividido em {nume[3]} unidades,'
              f' {nume[2]} dezenas, {nume[1]} centenas e {nume[0]} milhares')

        break
    except KeyboardInterrupt:
        print('\033[91m\nO usuário parou o progama\033[0m')
        break

    except ValueError:
        print('\033[91mO valor adicionado não é um valor númerico.\033[0m')

    except:
        print('\033[91mO programa parou de funcionar, e o problema não foi identificado.\033[0m')
        break
