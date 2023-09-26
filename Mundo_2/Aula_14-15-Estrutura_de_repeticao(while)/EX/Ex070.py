# nice

while True:
    try:
        cont_1000 = cont = som = 0
        while True:
            nome = str(input('Nome do produto: ')).strip().title()
            preco = float(input('Preço do produto: R$'))
            cont += 1
            if preco > 1000:
                cont_1000 += 1
            som += preco
            if cont == 1:
                barato = preco
                nome_barato = nome
            elif preco < barato:
                barato = preco
                nome_barato = nome
            while True:
                resp = str(input('Quer continuar o progama? [S/N]  '))[0]
                if resp.upper() in 'SN':
                    break
                else:
                    print(f'\033[91mA resposta {resp}, não é uma das opções possiveis!\033[0m')
            if resp.upper() in 'N':
                break
        print(f'\033[92mO total gasto foi de R${som:.2f}\033[0m')
        print(f'\033[92m{cont_1000} produtos custam mais de R$1000,00\033[0m')
        print(f'\033[92mO produto mais barato foi {nome_barato} que custa R${barato:.2f}\033[0m')
        break
    except KeyboardInterrupt:
        print('\033[91m\nO usuário parou o progama\033[0m')
        break

    except ValueError:
        print('\033[91mO valor adicionado não é um valor númerico possivel.\033[0m')

    except Exception as erro:
        print(f'\033[91mO programa parou de funcionar, e o problema é {erro}.\033[0m')
        break
