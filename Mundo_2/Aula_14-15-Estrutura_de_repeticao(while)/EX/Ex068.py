from random import randint

while True:
    vitorias = 0
    try:
        while True:
            while True:
                jogador = str(input('Você escolhe impar[I] ou par[P]? '))[0].upper()
                if jogador in 'IP':
                    break
                print('\033[91mOpção inválida\033[0m')
            while True:
                numJog = int(input('Digite um valor: '))
                if 0 <= numJog <= 10:
                    break
                print(f'\033[91mComo você jogou {numJog}??\033[0m')
            numPC = randint(0, 10)
            soma = numJog + numPC
            if soma % 2 == 0:
                if jogador == "P":
                    print(f'Você jogou {numJog} e o computador {numPC}. Total de {soma} DEU PAR')
                    print('\033[92mVocê VENCEU!\033[0m')
                    vitorias += 1
                else:
                    print(f'Você jogou {numJog} e o computador {numPC}. Total de {soma} DEU PAR')
                    print('\033[91mVocê PERDEU!\033[0m')
                    break
            else:
                if jogador == "I":
                    print(f'Você jogou {numJog} e o computador {numPC}. Total de {soma} DEU IMPAR')
                    print('\033[92mVocê VENCEU!\033[0m')
                    vitorias += 1
                else:
                    print(f'Você jogou {numJog} e o computador {numPC}. Total de {soma} DEU IMPAR')
                    print('\033[91mVocê PERDEU!\033[0m')
                    break

        print('=-' * 20)
        print(f'Você ganhou {vitorias} vezes seguidas ')
        print('=-' * 20)
        break
    except ValueError:
        print('\033[91mO valor digitado não é um inteiro\033[0m')

    except KeyboardInterrupt:
        print('\033[91mO usuário interrompeu o programa.\033[0m')
        break

    except:
        print('\033[91mOcorreu um problema no programa\033[0m')