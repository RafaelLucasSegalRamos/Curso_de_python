from time import sleep

while True:
    try:
        while True:
            n1 = float(input('Digite o primeiro valor: '))
            n2 = float(input('Digite o segundo valor: '))
            while True:


                print('''\033[93mEscolha uma das opções abaixo:
                [1] Somar
                [2] Multiplicar
                [3] Maior
                [4] Novos números
                [5] Sair do programa\033[0m''')
                opcao = int(input('Qual é a sua opção? '))

                if opcao == 1:
                    result = n1 + n2
                    print(f'A soma entre {n1} + {n2} é igual a {result}')
                    sleep(2)
                elif opcao == 2:
                    result =  n1 * n2
                    print(f'A multiplicação entre {n1} x {n2} é igual a {result}')
                    sleep(2)
                elif opcao == 3:
                    if n1 > n2:
                        print(f'O número {n1} é maior que o número {n2}')
                    elif n1 < n2:
                        print(f'O número {n2} é maior que o número {n1}')
                    else:
                        print(f'O número {n1} é igual ao número {n2}')
                    sleep(2)
                elif opcao == 4:
                    n1 = float(input('Digite o primeiro valor: '))
                    n2 = float(input('Digite o segundo valor: '))
                elif opcao == 5:
                    print('Finalizando...')
                    sleep(2)
                    break


            while True:
                resp = str(input('Quer continuar? [S/N]  '))
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

    except:
        print('\033[91mO programa parou de funcionar, e o problema não foi identificado.\033[0m')
        break
