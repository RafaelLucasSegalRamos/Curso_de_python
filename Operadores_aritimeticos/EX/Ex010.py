
while True:
    try:
        brl = float(input('Digite o valor em real que serpa tranformado em dólar: '))

        Usl = brl/3.27

        print(f'De acordo com a transformção de valor (1 dolar = 3.27 brl) '
              f'o valor de R${brl:.2f} será R${Usl:.2f} dolar(es).')

        break
    except ValueError:
        print('\033[91mO valor digitado não é um valor inteiro.\033[0m')
    except KeyboardInterrupt:
        print('\033[95mO usuário parou o programa\033[0m')
        break
    except:
        print('Ocorreu algum erro não identificado.')