while True:
    try:
        preco = float(input('Digite o valor de um produto: '))

        desc = preco * 0.05

        predesc = preco - desc

        print(f'O desconto ficou de R${desc:.2f}, ou seja o preço atual é de R${predesc:.2f}')
    except KeyboardInterrupt:
        print('\033[91mO usuário parou o progama\033[0m')
        break

    except ValueError:
        print('\033[91mO valor adicionado é um valor númerico.\033[0m')

    except:
        print('\033[91mO programa parou de funcionar, e o problema não foi identificado.\033[0m')
