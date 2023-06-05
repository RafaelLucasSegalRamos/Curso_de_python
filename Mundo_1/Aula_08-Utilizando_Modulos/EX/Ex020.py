import random

alunos = list()

while True:
    try:
        while True:
            aluno = str(input('Digite um dos nomes que serão sorteados: '))

            alunos.append(aluno)
            while True:
                resp = str(input('Dejesa continuar? [S/N]  '))
                if resp in 'Ss':
                    break
                elif resp in 'Nn':
                    break
                else:
                    print('\033[91mO valor digitado não é uma das opções acima.\033[0m')
            if resp in 'Nn':
                break
        random.shuffle(alunos)
        print(f'A ordem será {alunos}')

        break
    except KeyboardInterrupt:
        print('\033[91m\nO usuário parou o progama\033[0m')
        break

    except ValueError:
        print('\033[91mO valor adicionado não é um valor númerico.\033[0m')

    except:
        print('\033[91mO programa parou de funcionar, e o problema não foi identificado.\033[0m')
        break
