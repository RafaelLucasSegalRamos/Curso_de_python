while True:
    nomes = list()
    listGen = list()
    idadeSoma = 0
    numMulherNova = 0
    try:
        while True:
            for c in range(1, 5):
                nome = str(input(f'\033[95mDigite o {c}º nome: '))
                nomes.append(nome)
                idade = int(input(f'\033[95mDigite a idade do(a) {nome}: '))
                if c == 1:
                    idadeMax = idade
                    nomeMax = nome
                while True:
                    gen = str(input(f'\033[95mDigite o gênero do {nome} nome:[F/M] ')).lower()
                    if gen in 'fm':
                        break
                    else:
                        print('\033[91mDigite se você nasceu do sexo masculino ou do sexo feminino.')

                if gen == 'm' and idade > idadeMax:
                    idadeMax = idade
                    nomeMax = nome
                elif gen == 'f' and idade < 20:
                    numMulherNova += 1

                listGen.append(gen)
                idadeSoma += idade
            medIdade = idadeSoma / len(nomes)
            print(f'\033[94mA média de idade do grupo é {medIdade:.2f} anos.')
            print(f'\033[93mO homem mais velho tem {idadeMax} anos e se chama {nomeMax}.')
            print(f'\033[92mO número de mulheres com menos de 20 anos é {numMulherNova}.')
            while True:
                resp = str(input('\033[95mQuer continuar verificandos dados?[S/N]: ')).lower()
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
