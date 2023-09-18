s = 0

while True:
    try:
        for i in range(1, 7):
            num = int(input(f'\033[97mDigite o {i}º número: '))
            if num % 2 == 0:
                s += num
        print(f'\033[92m\nA soma dos números pares é: {s}')
        break
    except KeyboardInterrupt:
        print('\033[91m\nO usuário interrompeu o progama.')
        break

    except:
        print('\033[91m\nOcorreu um erro não identificado.')
