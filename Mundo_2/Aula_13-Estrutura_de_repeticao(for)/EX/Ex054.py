import datetime
maior = 0
menor = 0

while True:
    try:
        while True:
            ano = datetime.date.today().year

            for i in range(0, 7):
                anonas = int(input(f'\033[97mDigite o ano de nascimento da {i + 1}ª pessoa: '))
                if ano - anonas >= 18:
                    maior += 1
                else:
                    menor += 1
            print(f'\033[92m{maior} pessoas das 7 digitadas, atingiram a maior idade.')
            while True:
                resp = str(input('\033[95mQuer continuar contando quantas pessoas atingiram a maior idade?[S/N]: ')).lower()
                if resp in 'sn':
                    break
            if resp == 'n':
                break
        break
    except KeyboardInterrupt:
        print('\033[91m\nO usuário interrompeu o progama.')
        break

    except:
        print('\033[91m\nOcorreu um erro não identificado.')
