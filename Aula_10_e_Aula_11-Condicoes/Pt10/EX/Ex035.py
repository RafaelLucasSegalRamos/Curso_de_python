while True:
    try:
        retas = list()

        for c in range(1, 4):
            retas.append(int(input('Digite o tamanho de uma reta: ')))

        if retas[0] >= retas[2] + retas[1] or retas[1] >= retas[2] + retas[0] or retas[2] >= retas[0] + retas[1]:
            print('Este conjunto de retas não podem formar um triângulo')
        else:
            if retas[0] == retas[1] == retas[2]:
                print('Essa retas podem formar um triangulo, e será um triangulo equilátero!')
            elif retas[0] == retas[1] != retas[2] or retas[2] == retas[1] != retas[0] or retas[0] == retas[2] != retas[1]:
                print('Essa retas podem formar um triangulo, e será um triangulo isósceles!')
            elif retas[0] != retas[1] != retas[2]:
                print('Essa retas podem formar um triangulo, e será um triangulo escaleno!')

        break
    except KeyboardInterrupt:
        print('\033[91m\nO usuário parou o progama\033[0m')
        break

    except ValueError:
        print('\033[91mO valor adicionado não é um valor númerico.\033[0m')

    except:
        print('\033[91mO programa parou de funcionar, e o problema não foi identificado.\033[0m')
        break
