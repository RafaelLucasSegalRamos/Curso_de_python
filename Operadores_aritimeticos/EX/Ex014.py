while True:
    try:
        Kilometro = float(input('Digite a quantidade de Km percorridos pelo carro alugado: '))

        dias = int(input('Digite por quantos dias o carro foi alugado: '))

        precodia = dias * 60

        precokm = Kilometro * 0.15

        precofn = precokm + precodia

        print(f'A valor dos dias alugados do carro é R${precodia:.2f},\n'
              f' e os quilometros rodados custaram R${precokm:.2f},\n'
              f' e por isso o preço final foi: R${precofn:.2f}')

        break
    except KeyboardInterrupt:
        print('\033[91m\nO usuário parou o progama\033[0m')
        break

    except ValueError:
        print('\033[91mO valor adicionado é um valor númerico.\033[0m')

    except:
        print('\033[91mO programa parou de funcionar, e o problema não foi identificado.\033[0m')
