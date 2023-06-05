while True:
    try:
        salario = float(input('Digite o valor do salário do comprador: R$'))
        valor_casa = float(input('Digite o valor da casa: R$'))
        while True:
            quant_meses = int(input('Digite em quantos meses esse valor será pago: '))
            if quant_meses > 12:
                print('\033[31mO preço da casa só pode ser pago no maximo em um ano\033[m')
            else:
                break
        if salario*0.30 <= valor_casa/quant_meses:
            print('\033[31mSeu salário é muito baixo, é recomendado que não compre está casa!\033[m')
        else:
            print(f'\033[32mMuito bem! O preço a se pagar por mês será R${valor_casa/quant_meses:.2f}')
            break
    except KeyboardInterrupt:
        print('\033[31mO usuário interrompeu o progama.\033[m')
        break
    except ValueError:
        print('\033[31mEste valor não condiz com o que foi pedido.\033[m')
    except:
        print('\033[31mOcorreu um erro não identificado.\033[m')