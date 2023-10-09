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
        print('-'*40)
        print(f'{"MENU PRINCIPAL":^40}')
        print('-'*40)
        print(f'{"1 - Ver pessoas cadastradas":<40}')
        print(f'{"2 - Cadastrar nova pessoa":<40}')
        print(f'{"3 - Sair do sistema":<40}')
        print('-'*40)
        opcao = int(input('Sua opção: '))
        sleep(1.5)
        if opcao == 2:
            nome = str(input('Nome: ').capitalize())
            idade = int(input('Idade: '))
            cadastrar(nome, idade, arq)

        elif opcao == 1:
            print('-'*40)
            print(f'{"PESSOAS CADASTRADAS":^40}')
            print('-'*40)
            print(f'{"NOME":<30}{"IDADE":<10}')
            linhas = Ex115.lerArquivo(arq)
            for linha in linhas:
                linha = linha.split(';')
                print(f'{linha[0]:<30}{linha[1]:<10}')
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

