while True:
    try:
        while True:
            for c in range(1, 6):
                peso = float(input(f'\033[95mDigite o peso da {c}ª pessoa: '))
                if c == 1:
                    maior = peso
                    menor = peso
                else:
                    if peso > maior:
                        maior = peso
                    if peso < menor:
                        menor = peso
            print(f'\033[92mO mai peso foi {maior}Kg e o men foi {menor}Kg.')
            while True:
                resp = str(input('\033[95mQuer continuar qual pessoa tem o mai peso e o men?[S/N]: ')).lower()
                if resp in 'sn':
                    break
            if resp == 'n':
                break
        break
    except KeyboardInterrupt:
        print('\033[91m\nO usuário interrompeu o progama.')
        break

    except:
        print('\033[91m\nOcorreu um erro não identificado.')
