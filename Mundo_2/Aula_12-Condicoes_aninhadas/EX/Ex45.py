import random
from time import sleep

while True:
    try:
        print('\033[96mVamos jogar pedra, papel ou tesoura! (Ou jokenpô para outros)\033[m')
        esc = int(input('Faça sua esolha baseado no número ao lado:'
                        '\n[1]Pedra,'
                        '\n[2]Papel,'
                        '\n[3]Tesoura'
                        '\n\033[92mVocê escolheu: '))
        IA_esc = random.randint(1, 3)
        lista = ['Pedra', 'Papel', 'Tesoura']
        sleep(0.75)
        print('Jo...')
        sleep(0.75)
        print('ken...')
        sleep(0.75)
        print('Pô!!')
        sleep(0.75)
        if esc == IA_esc:
            print(f'\033[97mOpa! Houve um empate! Pois você escolheu {esc} e eu {IA_esc}')
            sleep(2)
        elif (esc == 1 and IA_esc == 2) or (esc == 2 and IA_esc == 3) or (esc == 3 and IA_esc == 1):
            print(f'\033[31mVocê Perdeu! Eu escolhi {lista[IA_esc-1]} enquanto você escolheu {lista[esc-1]}\033[m')
            sleep(2)
        elif (esc == 2 and IA_esc == 1) or (esc == 3 and IA_esc == 2) or (esc == 1 and IA_esc == 3):
            print(f'\033[96mEssa não eu perdi! Eu escolhi {lista[IA_esc-1]} enquanto você escolheu {lista[esc-1]}\033[m')
            sleep(2)
        else:
            print('\033[91mEssa não é uma das opções possiveis!!\033[0m')
        while True:
            esco = str(input('Você quer continuar?'))
            if esco.upper() in 'SN':
                break
            else:
                print('\033[91mEssa não é uma das opções deisponiveis!!\033[m')
        if esco.upper() == 'N':
            break
    except KeyboardInterrupt:
        print('\033[91m\nO usuário interrompeu o progama.')
        break
    except:
        print('\033[91m\nOcorreu um erro não identificado.')
