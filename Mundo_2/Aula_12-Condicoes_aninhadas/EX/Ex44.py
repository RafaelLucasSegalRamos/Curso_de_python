while True:
    try:
        preco_normal = float(input("Digite o valor cheio do produto: R$"))
        while True:
            esc = int(input('Escolha uma forma de pagamento de acordo com as seguintes opções:'
                            '\n\033[95m[1] Dinheiro/Cheque, desconto de 10%'
                            '\n[2] A vista no cartão, desconto de 5%'
                            '\n[3] Em até 2x no cartão, preço normal'
                            '\n[4] 3x ou mais no cartão, 20% de juros simples.'
                            '\n\033[mEscreva a seguir uma das opções(Os números que cada uma representa): '))
            if esc == 1:
                preco_final = preco_normal - (preco_normal * 0.1)
                break
            elif esc == 2:
                preco_final = preco_normal - (preco_normal * 0.05)
                break
            elif esc == 3:
                preco_final = preco_normal
                break
            elif esc == 4:
                preco_final = preco_normal + (preco_normal * 0.2)
                break
            else:
                print('\033[91mEssa não era uma das opções possiveis!!\033[m')

        print(f'De acordo com as opções escolhida você terá que pagar R${preco_final:.2f}')
        while True:
            resp = str(input('Quer continuar? [S/N] ')).upper()
            if resp in 'SN':
                break
            else:
                print('\033[31mEstá não é uma das respostas possiveis!!\033[m')
        if resp in 'N':
            break

    except KeyboardInterrupt:
        print('\033[31mO usuário interrompeu o progama.\033[m')
        break
    except ValueError:
        print('\033[31mEste valor não condiz com o que foi pedido.\033[m')
    except:
        print('\033[31mOcorreu um erro não identificado.\033[m')
