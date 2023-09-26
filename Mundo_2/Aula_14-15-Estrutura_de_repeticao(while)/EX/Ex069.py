# nice

while True:
    try:
        cont_h = 0
        cont_18 = 0
        cont_m_20 = 0
        while True:
            while True:
                idade = int(input('Qual a sua idade?  '))
                while True:
                    sexo = str(input('Qual o seu sexo? [M/F]  '))[0].upper()
                    if sexo in 'MF':
                        break
                    else:
                        print(f'\033[91mA resposta {sexo}, não é uma das opções possiveis!\033[0m')
                if sexo in 'M':
                    cont_h += 1
                if idade >= 18:
                    cont_18 += 1
                if sexo in 'F' and idade < 20:
                    cont_m_20 += 1

                while True:
                    respo = str(input('Quer continuar adicionando pessoas? [S/N]  '))
                    if respo.upper() in 'S':
                        break
                    elif respo.upper() in 'N':
                        break
                    else:
                        print(f'\033[91mA resposta {respo}, não é uma das opções possiveis!\033[0m')
                if respo.upper() in 'N':
                    break
            print(f'Foram adicionados {cont_h} homens, {cont_18} pessoas com mais de 18 anos e {cont_m_20} mulheres com menos de 20 anos.')
            while True:
                resp = str(input('Quer continuar o progama? [S/N]  '))[0]
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

    except Exception as erro:
        print(f'\033[91mO programa parou de funcionar, e o problema é {erro}.\033[0m')
        break
