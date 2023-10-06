from time import sleep
from Modulos import Ex115
dic = {}
dados = {}
cont = 0
arq = 'Ex115.txt'

if Ex115.arquivoExiste(arq):
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não encontrado.')
    Ex115.criarArquivo(arq)
while True:
    try:

        cont += 1
        print('-'*30)
        print(f'{"MENU PRINCIPAL":^30}')
        print('-'*30)
        print(f'{"1 - Ver pessoas cadastradas":<30}')
        print(f'{"2 - Cadastrar nova pessoa":<30}')
        print(f'{"3 - Sair do sistema":<30}')
        print('-'*30)
        opcao = int(input('Sua opção: '))
        sleep(1.5)
        if opcao == 2:
            dados['nome'] = str(input('Nome: ').capitalize())
            dados['idade'] = int(input('Idade: '))
            dic[f'pessoa{cont}'] = dados.copy()

        elif opcao == 1:
            print('-'*30)
            print(f'{"PESSOAS CADASTRADAS":^30}')
            print('-'*30)
            print(f'{"NOME":<20}{"IDADE":<10}')
            for c in dic:
                print(f'{dic[c]["nome"]:<20}{dic[c]["idade"]:<10}')
                sleep(0.5)
        elif opcao == 3:
            print('Saindo do sistema...')
            break
        else:
            print('Opção inválida! Tente novamente.')

    except KeyboardInterrupt:
        print('O usuário preferiu não informar os dados.')
        sleep(1.5)
        break
    except ValueError:
        print('Erro! O valor enviado não corresponde ao tipo pedido.')
        sleep(1.5)
        continue
    except:
        print('Erro! Tente novamente.')
        sleep(1.5)

